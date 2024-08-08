"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        hash1={}
        return self.temp(n,hash1)
    def temp(self,n: int,hash1: dict[int,int]) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        if n not in hash1:
            hash1[n]= self.temp(n-1,hash1)+self.temp(n-2,hash1)
        return hash1[n]
        