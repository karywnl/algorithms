class TrieNode:
    def __init__(self):
        self.children = {}  # Maps each letter to another TrieNode
        self.freq = None    # A number here means a complete word ends here


root = TrieNode()  # The starting node, before any letters
