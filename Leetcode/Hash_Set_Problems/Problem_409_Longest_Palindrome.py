"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp=Counter(s)
        print(temp)
        total=0
        odd=False
        for key,value in temp.items():
            if value%2==0:
                total=total+value
            else :  
                odd=True
                total=total+(value-1)
            
        if odd==True: 
            return total+1
        else:
            return total
       

    
    



        