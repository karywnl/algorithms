"""Ordinary trie and the measurements for the lab record.

Run: python3 lab6/trie.py count_1w.txt
The dataset is available at https://www.norvig.com/ngrams/count_1w.txt.
"""

import gc
import json
import platform
import random
import statistics
import string
import sys
from time import perf_counter


class TrieNode:
    def __init__(self, alphabet, use_array):
        self.children = [None] * len(alphabet) if use_array else {}
        self.label = ""  # Compressed tries store an edge label here.
        self.freq = None  # None means that no complete word ends here.


class Trie:
    def __init__(self, alphabet=string.ascii_lowercase, use_array=False):
        self.alphabet = alphabet
        self.use_array = use_array
        self.index = {char: i for i, char in enumerate(alphabet)}
        self.root = self.new_node()

    def new_node(self):
        return TrieNode(self.alphabet, self.use_array)

    def get_child(self, node, char):
        if self.use_array:
            return node.children[self.index[char]]
        return node.children.get(char)

    def set_child(self, node, char, child):
        key = self.index[char] if self.use_array else char
        node.children[key] = child

    def child_nodes(self, node):
        children = node.children if self.use_array else node.children.values()
        return [child for child in children if child is not None]

    def insert(self, word, freq):
        if any(char not in self.index for char in word):
            raise ValueError("Word contains a character outside the alphabet")
        node = self.root
        for char in word:
            child = self.get_child(node, char)
            if child is None:
                child = self.new_node()
                child.label = char
                self.set_child(node, char, child)
            node = child
        node.freq = freq

    def find_prefix(self, prefix):
        node = self.root
        word = ""
        while prefix:
            if prefix[0] not in self.index:
                return None, ""
            child = self.get_child(node, prefix[0])
            if child is None:
                return None, ""
            # A prefix may finish inside a compressed edge.
            if child.label.startswith(prefix):
                return child, word + child.label
            if not prefix.startswith(child.label):
                return None, ""
            prefix = prefix[len(child.label):]
            word += child.label
            node = child
        return node, word

    def search(self, word):
        node, matched = self.find_prefix(word)
        return node is not None and matched == word and node.freq is not None

    def startsWith(self, prefix):
        node, word = self.find_prefix(prefix)
        return node is not None

    def autocomplete(self, prefix, k):
        node, word = self.find_prefix(prefix)
        if node is None or k <= 0:
            return []
        matches = []
        stack = [(node, word)]
        while stack:
            node, word = stack.pop()
            if node.freq is not None:
                matches.append((word, node.freq))
            for child in self.child_nodes(node):
                stack.append((child, word + child.label))
        # Higher frequency first; alphabetical order breaks ties.
        matches.sort(key=lambda item: (-item[1], item[0]))
        return matches[:k]

    def measurements(self):
        """Count nodes, retained Python object bytes and slots at each depth."""
        seen = set()
        memory = 0

        def count_object(obj):
            nonlocal memory
            if id(obj) not in seen:
                seen.add(id(obj))
                memory += sys.getsizeof(obj)

        count_object(self)
        count_object(self.__dict__)
        count_object(self.alphabet)
        count_object(self.use_array)
        count_object(self.index)
        for char, index in self.index.items():
            count_object(char)
            count_object(index)
        count_object(None)
        depths = {}
        nodes = 0
        stack = [(self.root, 0)]
        while stack:
            node, depth = stack.pop()
            nodes += 1
            for obj in (node, node.__dict__, node.children, node.label, node.freq):
                count_object(obj)
            if not self.use_array:
                for char in node.children:
                    count_object(char)
            children = self.child_nodes(node)
            if depth not in depths:
                depths[depth] = [0, 0]
            depths[depth][0] += 1
            depths[depth][1] += len(children)
            for child in children:
                stack.append((child, depth + len(child.label)))
        return nodes, memory / 1024**2, depths


def load_words(filename):
    words = []
    with open(filename) as file:
        for line in file:
            word, freq = line.split()
            if all(char in string.ascii_lowercase for char in word):
                words.append((word, int(freq)))
    words.sort(key=lambda item: -item[1])
    if len(words) < 100000:
        raise ValueError("Dataset must contain at least 100000 valid words")
    return words[:100000]


def time_queries(operation, queries, repeats=5):
    times = []
    for repeat in range(repeats):
        start = perf_counter()
        for query in queries:
            operation(query)
        times.append((perf_counter() - start) * 1000000 / len(queries))
    return statistics.median(times)


def run(filename):
    # Import here so compressed_trie.py can reuse Trie without a circular import.
    from compressed_trie import CompressedTrie

    words = load_words(filename)
    rng = random.Random(42)
    present = [word for word, freq in rng.sample(words, 1000)]
    absent = [word + "zzzzzz" for word in present]
    prefixes = ["progr", "comp", "data", "art", "uni"]
    versions = [("Trie array", Trie, True), ("Trie dictionary", Trie, False),
                ("Compressed array", CompressedTrie, True),
                ("Compressed dictionary", CompressedTrie, False)]
    result = {"python": platform.python_version(), "system": platform.platform(),
              "word_count": len(words), "english": [], "random": [],
              "slots": {}, "suggestions": {}}
    for name, structure, use_array in versions:
        gc.collect()
        trie = structure(use_array=use_array)
        start = perf_counter()
        for word, freq in words:
            trie.insert(word, freq)
        build = perf_counter() - start
        assert all(trie.search(word) for word, freq in words)
        assert not any(trie.search(word) for word in absent)
        suggestions = {}
        for prefix in prefixes:
            expected = sorted([item for item in words if item[0].startswith(prefix)],
                              key=lambda item: (-item[1], item[0]))[:5]
            suggestions[prefix] = trie.autocomplete(prefix, 5)
            assert suggestions[prefix] == expected
        nodes, memory, depths = trie.measurements()
        result["english"].append({"name": name, "nodes": nodes, "memory": memory,
                                  "build": build,
                                  "present": time_queries(trie.search, present),
                                  "absent": time_queries(trie.search, absent),
                                  "autocomplete": time_queries(
                                      lambda p: trie.autocomplete(p, 5), prefixes)})
        if use_array:
            result["slots"][name] = depths
        result["suggestions"][name] = suggestions
        del trie

    for alphabet in ["ACGT", string.ascii_lowercase,
                     string.ascii_letters + string.digits,
                     "".join(chr(i) for i in range(32, 127))]:
        # The same 10000 length-12 strings go into all four versions.
        rng = random.Random(42)
        samples = ["".join(rng.choices(alphabet, k=12)) for i in range(10000)]
        for name, structure, use_array in versions:
            gc.collect()
            trie = structure(alphabet, use_array)
            for word in samples:
                trie.insert(word, 1)
            nodes, memory, depths = trie.measurements()
            result["random"].append({"alphabet": len(alphabet), "name": name,
                                     "nodes": nodes, "memory": memory})
            del trie
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "count_1w.txt")
