class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


trie = Trie()


words_to_insert = ["apple", "banana", "orange", "app", "applet"]
for word in words_to_insert:
    trie.insert(word)


words_to_search = ["apple", "app", "banana", "grape"]
for word in words_to_search:
    if trie.search(word):
        print(f"{word} found in the trie")
    else:
        print(f"{word} not found in the trie")
