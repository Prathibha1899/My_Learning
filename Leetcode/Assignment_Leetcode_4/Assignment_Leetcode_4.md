**Problem statement**:<br>
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.<br>

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.<br>

**Example 1**:<br>

![alt text](image.png)<br>

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22<br>
Output: [[5,4,11,2],[5,8,4,5]]<br>
Explanation: There are two paths whose sum equals targetSum:<br>
5 + 4 + 11 + 2 = 22<br
5 + 8 + 4 + 5 = 22<br>

**Solution**:
~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSumUtil(self, root, targetSum, current_path, matching_paths):
        if root is None:
            return

        current_path.append(root.val)

        if root.val == targetSum and root.left is None and root.right is None:
            matching_paths.append(list(current_path)) # You have to do a deep copy, otherwise current_path.pop() will modify it
        else:
            self.pathSumUtil(root.left, targetSum - root.val, current_path, matching_paths)
            self.pathSumUtil(root.right, targetSum - root.val, current_path, matching_paths)
        current_path.pop()#backtracing

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        matching_paths = []
        self.pathSumUtil(root, targetSum, [], matching_paths)
        return matching_paths
        
        
~~~

**Question 1**:<br>
**Explain how each recursion has global information**<br>
The recursive solution keeps track of the current path and all valid paths that sum to the target using two lists, curr_path and matching_paths. curr_path stores the path from the root to the current node, updating as the function goes deeper into the tree and backtracking as it returns. matching_paths stores all paths that add up to the target sum. When the function finds a leaf node with the correct sum, it adds a copy of curr_path to matching_paths. By maintaining these lists as parameters in the recursive function, the solution ensures that each recursive call has access to the global state necessary to build and track paths and their sums.<br>

**Question 2**:<br>
**Explain why DFS instead of BFS**<br>

**DFS**:<br>
Depth-First Search (DFS) is a method for exploring a tree or graph. It starts at the root (or any starting point) and explores as far as possible along each branch before backtracking. In simple terms, it goes deep into one path until it can't go any further, then moves back and tries the next path. This process continues until all paths have been explored.<br>

**BFS**:<br>
Breadth-First Search (BFS) is a method for exploring a tree or graph. It starts at the root (or any starting point) and explores all the neighbors at the present depth before moving on to nodes at the next depth level. In simple terms, it looks at all nodes level by level, starting from the root and moving outward.<br>

DFS is better than BFS for this problem because it follows one path from the root to a leaf at a time, making it easier to keep track of the current path and its sum. It also allows us easy backtracing which is essential for finding all the root-to-leaf paths.<br>

**Question 3**:<br>
**Explain what backtrace is and why you need it**<br>
Backtracing is technique primarly used in tree/graph concept to explore all potential solutions of the given problem. what we basically do here is, we try a path and if it doesn't work, we backtrack to the last choice and choose another path. In this way we will be able to look into all the paths of the given graph and get our solutions. Therefore this method  ensures that every possible solution is considered while efficiently discarding paths that can't lead to a solution.


