"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 
"""

class Solution:
    def groupAnagrams(self, strs):
        output=(list)
        for ele in strs:
            sum1=[0]*26
            for char in ele:
                sum1[ord(char)-ord('a')]=sum1[ord(char)-ord('a')]+1
            output[tuple(sum1)].append(ele)
        return output.values()

        