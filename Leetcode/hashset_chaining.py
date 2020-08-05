class MyHashSet:
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
            
    def __init__(self,size=1000):
        """
        Initialize your data structure here.
        """
        self._size = size
        self._hashtable = [None]*self._size
    
    def _hashcode(self,key):
        return key % self._size
    
    def add(self, key: int) -> None:
        hashcode = self._hashcode(key)
        
        if(not self._hashtable[hashcode]):
            firstnode = self.Node(key)
            self._hashtable[hashcode] = firstnode
        else:
            head = self._hashtable[hashcode]
            if(head.val == key):
                return
            while(head.next):
                head = head.next
                if(head.val == key):
                    return
                
            head.next = self.Node(key)

    def remove(self, key: int) -> None:
        hashcode = self._hashcode(key)
        head = self._hashtable[hashcode]
        if not head:
            return
        if(head.val == key):
            self._hashtable[hashcode] = head.next
            return
        while(head.next):
            prev = head
            head = head.next
            if(head.val == key):
                prev.next = head.next
                return        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashcode = self._hashcode(key)
        if(not self._hashtable[hashcode]):
            return False
        else:
            head = self._hashtable[hashcode]
            if(head.val == key):
                return True
            while(head.next):
                head = head.next
                if(head.val == key):
                    return True
            return False
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)