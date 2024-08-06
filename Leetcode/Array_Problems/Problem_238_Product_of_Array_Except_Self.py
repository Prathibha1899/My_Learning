"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution:
    def productExceptSelf(self, nums):
        product=1
        new=[]
        for ele in nums:
            new.append(product)
            product=product*ele
        product=1
        for index in range(len(nums)-1,-1,-1):
            new[index]=new[index]*product
            product=product*nums[index]
        return new