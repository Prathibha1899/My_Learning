"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        for i in s:
            if i in hash1:
                hash1[i]=hash1[i]+1
            else:
                hash1[i]=0
        for i in t:
            if i in hash2:
                hash2[i]=hash2[i]+1
            else:
                hash2[i]=0
        if (hash1==hash2):
            return True
        else:
            return False

        