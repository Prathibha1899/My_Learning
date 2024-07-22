"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r=0
        len1=len(word1)
        len2=len(word2)
        res=''
        while l<len1 and r<len2:
            res=res+word1[l]+word2[r]
            l=l+1
            r=r+1
        while l<len1:
            res=res+word1[l]
            l=l+1
        while r<len2:
            res=res+word2[r]
            r=r+1
        return res
            
        








