"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp=Counter(magazine)
        for key,value in Counter(ransomNote).items():
            if key not in temp:
                return False
            elif value>temp[key]:
                return False
        return True
ransomNote = "a"
magazine = "b"
Solution().canConstruct(ransomNote,magazine)


        