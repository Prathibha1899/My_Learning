"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        long=0
        for i in range(length):
            curr=s[i]
            seen=set(curr)
            j=i+1
            while j<length:
                next_val=s[j]
                if next_val not in seen:
                    seen.add(next_val)
                else:
                    break
                j=j+1
            if len(seen)>long:
                long=len(seen)
        return long