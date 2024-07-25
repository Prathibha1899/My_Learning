"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    def sortedSquares(self, nums):
        left=0
        n=len(nums)
        right=n-1
        res=[None]*n
        res_index=n-1
        while left<=right:
            left_square=nums[left]*nums[left]
            right_square=nums[right]*nums[right]
            if left_square>right_square:
                res[res_index]=left_square
                left=left+1
            else:
                res[res_index]=right_square
                right=right-1
            res_index=res_index-1
        return res
                
            
        