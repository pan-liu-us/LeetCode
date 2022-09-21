# Complexity Analysis:

# insert
# Time complexity : O(m), 
    # Where m is the key length.
# Space complexity : O(m)
    # In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add m new nodes

# search & startsWith
# Time complexity : O(m)
# Space complexity : O(1)

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
     
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node 
        
        
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)