"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) :
        return self.pathsum2(root,targetSum,[],[])

    def pathsum2(self,root, targetSum: int,curr_path,matching_paths):
        if root is None:
            return
        curr_path.append(root.val)
        if root.val==targetSum and root.left is None and root.right is None:
            matching_paths.append(list(curr_path))
        else:
            self.pathsum2(root.left,targetSum-root.val,curr_path,matching_paths)
            self.pathsum2(root.right,targetSum-root.val,curr_path,matching_paths)
        curr_path.pop()
        return matching_paths
        
        