"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        length=len(lst)
        if length==0:
            return True
        elif length%2==0:
            first=lst[:length//2]
            last=lst[length:length//2-1:-1]
            if (first==last):
                return True
            else:
                return False

        else:
            first=lst[:length//2]
            last=lst[length:length//2:-1]
            if (first==last):
                return True
            else:
                return False