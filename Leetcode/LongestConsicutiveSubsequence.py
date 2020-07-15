

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicto = {}
        for i in nums:
            dicto[i] = 1
        
        max_cons_1 = 0
        for key in list(dicto.keys()):
            if(key-1 not in dicto):
                max_cons = 1
                while(key+1 in dicto):
                    max_cons+=1
                    key+=1
                max_cons_1 = max(max_cons_1,max_cons)
        return max_cons_1