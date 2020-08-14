# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)
        n=len(nums)
        res = nums[0]
        for i in range(1,n):
            out[i]*=res
            res*=nums[i]
        
        res = nums[len(nums)-1]
        for j in range(n-2,-1,-1):
            out[j]*=res
            res*=nums[j]
        return out