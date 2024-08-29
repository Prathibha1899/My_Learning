"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
nput: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root is None:
            return False
        if root.val==targetSum and root.left is None and root.right is None:
            return True
        return self.hasPathSum( root.left, targetSum-root.val) or self.hasPathSum( root.right, targetSum-root.val)