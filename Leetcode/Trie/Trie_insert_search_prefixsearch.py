class TrieNode:
    def __init__(self):
        self.keys = {}
        self.endNode = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currentNode = self.root
        for i in word:
            if i not in currentNode.keys.keys():
                currentNode.keys[i] = TrieNode()
            currentNode = currentNode.keys[i]
        currentNode.endNode = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentNode = self.root
        if(not len(word) and currentNode.endNode):
            return True
        elif(not len(word)):
            return False

        for ind,val in enumerate(word):
            if val not in currentNode.keys.keys():
                return False
            else:   
                currentNode=currentNode.keys[val]
        if(currentNode.endNode):
            return True
        return False
        

    def startsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentNode = self.root
        if(not len(word)):
            return True
        for ind,val in enumerate(word):
            if val not in currentNode.keys.keys():
                return False
            else:   
                currentNode=currentNode.keys[val]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)