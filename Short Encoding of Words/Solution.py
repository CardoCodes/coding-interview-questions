class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ends = [] #(TrieNode(), length)

    def insert(self, word):
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        self.ends.append((root,len(word)+1))

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        t = Trie()
        for w in words:
            t.insert(w[::-1])
        return sum([depth for node,depth in t.ends if len(node.children) == 0])

