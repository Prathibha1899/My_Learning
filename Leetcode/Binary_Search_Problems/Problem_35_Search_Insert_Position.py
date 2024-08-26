"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        mid=0
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        if target>nums[mid]:
            return mid+1
        else:
            return mid


        