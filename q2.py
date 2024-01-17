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

    def words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        words = []
        self._collect_words(node, prefix, words)
        return words

    def _collect_words(self, node, current_word, result):
        if node.is_end_of_word:
            result.append(current_word)

        for char, child_node in node.children.items():
            self._collect_words(child_node, current_word + char, result)


trie = Trie()


words_to_insert = ["apple", "banana", "orange", "app", "applet"]
for word in words_to_insert:
    trie.insert(word)

prefix_to_search = "app"
found_words = trie.words_with_prefix(prefix_to_search)

print(f"Words with prefix '{prefix_to_search}': {found_words}")
