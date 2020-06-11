# Given an array with n objects colored red, white or blue, sort them in-place so that objects of 
# the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,ind=0,0
        high=len(nums)-1
        
        while(ind<=high):
            if(nums[ind]==0):
                nums[ind],nums[low] = nums[low],nums[ind]
                ind+=1
                low+=1
            elif(nums[ind]==1):
                ind+=1
            else:
                nums[ind],nums[high] = nums[high],nums[ind]
                high-=1