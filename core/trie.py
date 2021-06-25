class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False
        self.path_list = []
        self.counter = 0


class Trie:
    def __init__(self, word_map):
        self.root = TrieNode("")
        self.word_map = word_map
        self.output = []

    def insert(self, word: str):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
        node.path_list = self.word_map[word]
        node.counter += 1

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.path_list))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def search(self, x: str) -> list:

        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])
        return sorted(self.output, key=lambda x: x[1], reverse=True)
