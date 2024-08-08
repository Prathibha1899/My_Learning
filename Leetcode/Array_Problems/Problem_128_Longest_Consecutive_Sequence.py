"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution:
    def longestConsecutive(self, nums):
        nums_set=set(nums)
        max_len=0
        for ele in nums:
            count=0
            if ele-1 not in nums_set:
                curr=ele
                count=1
                while curr+1 in nums_set:
                    curr=curr+1
                    count=count+1
            max_len=max(max_len,count)
        return max_len
