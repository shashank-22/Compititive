# Every operation should be in O(1) complexity

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(not val in self.hashmap):
            self.arr.append(val)
            self.hashmap[val] = len(self.arr)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if(val in self.hashmap):
            length = len(self.arr)
            ind = self.hashmap[val]
            self.hashmap[self.arr[length-1]] = ind
            self.arr[ind],self.arr[length-1] = self.arr[length-1], self.arr[ind]
            self.arr.pop(length-1)
            self.hashmap.pop(val)
            return True
        return False
            
        

    def getRandom(self) -> int:

        """
        Get a random element from the set.
        """
        rand = random.randint(0,len(self.arr)-1)
        return self.arr[rand]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()