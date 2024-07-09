"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        output=False
        open_brackets={'(':')','[':']','{':'}'}
        close_brackets={')':'(',']':'[','}':'{'}
        for i in s:
            if i in open_brackets:
                stack.append(i)
                output=False
            if i in close_brackets:
                try:
                    temp=stack.pop()
                    if temp==close_brackets[i]:
                        output=True
                    else:
                        return False
                except Exception as error:
                    return False
        if len(stack)!=0:
            return False
        return output

        