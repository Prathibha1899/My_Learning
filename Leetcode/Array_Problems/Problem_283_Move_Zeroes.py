"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=1
        if(len(nums)>1):   
            while right<len(nums):
                if nums[left]==0:
                    if nums[right]!=0:
                        nums[left],nums[right]=nums[right],nums[left]
                        left=left+1
                        right=right+1
                    else:
                        right=right+1
                else:
                    left=left+1
                    right=right+1

        

        