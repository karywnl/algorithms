"""Compressed trie: reuse traversal and measurement methods from Trie."""

from trie import Trie


class CompressedTrie(Trie):
    def insert(self, word, freq):
        if any(char not in self.index for char in word):
            raise ValueError("Word contains a character outside the alphabet")
        node = self.root
        while word:
            child = self.get_child(node, word[0])
            if child is None:
                child = self.new_node()
                child.label = word
                child.freq = freq
                self.set_child(node, word[0], child)
                return

            # Find the common part of the new word and existing edge.
            common = 0
            while (common < len(word) and common < len(child.label)
                   and word[common] == child.label[common]):
                common += 1
            if common == len(child.label):
                word = word[common:]
                node = child
                continue

            # Split the old edge at the point where the words diverge.
            middle = self.new_node()
            middle.label = child.label[:common]
            self.set_child(node, word[0], middle)
            child.label = child.label[common:]
            self.set_child(middle, child.label[0], child)
            word = word[common:]
            if word:
                leaf = self.new_node()
                leaf.label = word
                leaf.freq = freq
                self.set_child(middle, word[0], leaf)
            else:
                middle.freq = freq  # The new word ends inside the old edge.
            return
        node.freq = freq  # Also handles duplicate words and the empty word.


if __name__ == "__main__":
    trie = CompressedTrie()
    for word, freq in [("program", 50), ("programs", 20), ("progress", 30)]:
        trie.insert(word, freq)
    print("Search program:", trie.search("program"))
    print("Prefix progr:", trie.startsWith("progr"))
    print("Suggestions:", trie.autocomplete("progr", 5))
