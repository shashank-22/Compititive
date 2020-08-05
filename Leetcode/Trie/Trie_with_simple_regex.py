# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
class TrieNode:
    def __init__(self):
        self.keys = {}
        self.endNode = False
        
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currentNode = self.root
        for i in word:
            if i not in currentNode.keys.keys():
                currentNode.keys[i] = TrieNode()
            currentNode = currentNode.keys[i]
        currentNode.endNode = True
    
    
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def _recursivesearch(word,currentNode):
            if(not len(word) and currentNode.endNode):
                return True
            elif(not len(word)):
                return False

            for ind,val in enumerate(word):
                if(val != "." ):
                    if val not in currentNode.keys.keys():
                        return False
                    return _recursivesearch(word[ind+1:],currentNode.keys[val])
                else:
                    kk = False
                    for key in currentNode.keys.keys():
                        kk = _recursivesearch(word[ind+1:],currentNode.keys[key])
                        if(kk):
                            return kk
                    return False
        return _recursivesearch(word,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)