**Problem statement**:<br>
**Find Largest Value in Each Tree Row**<br>
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).<br>

**Example:**<br>

![alt text](largest_e1.jpg)<br>

Input: root = [1,3,2,5,3,null,9]<br>
Output: [1,3,9]<br>

**Solution**:<br>

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
      
        if root is None:
            return result
        queue = []    
        queue.append(root)
        while queue:
            currentLevelSize = len(queue)
            currentLevelMax = float('-inf')
            for _ in range(currentLevelSize):
                currentNode = queue.pop(0)
                currentLevelMax = max(currentLevelMax, currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(currentLevelMax)
        return result
~~~

**Question 1**:<br>
**Explain why BFS instead of DFS**?

**DFS**:<br>
Depth-First Search (DFS) is a method for exploring a tree or graph. It starts at the root (or any starting point) and explores as far as possible along each branch before backtracking. In simple terms, it goes deep into one path until it can't go any further, then moves back and tries the next path. This process continues until all paths have been explored.<br>

**BFS**:<br>
Breadth-First Search (BFS) is a method for exploring a tree or graph. It starts at the root (or any starting point) and explores all the neighbors at the present depth before moving on to nodes at the next depth level. In simple terms, it looks at all nodes level by level, starting from the root and moving outward.<br>

BFS (Breadth-First Search) is better for this problem than DFS because BFS processes the tree level by level, which is exactly what we need to find the largest value in each row. BFS uses a queue to keep track of nodes, ensuring all nodes at the current level are processed before moving to the next level. This makes it easier to find the maximum value for each level.


**Question 2**:<br>
**Explain why you need a queue and how it is used**<br>

A queue is used in this solution to help us process the tree level by level in a First-In-First-Out (FIFO) order. We start by putting the root node in the queue. Then, for each level, we take out each node, find the largest value among them, and add their children to the queue for the next level. The FIFO order ensures that we process all nodes at one level before moving to the next, which helps us easily find the largest value in each row of the tree.<br>

**Question 3**:<br>
**How is the max found for each level?**<br>

The maximum value for each level is found by starting with a variable set to a very low number. As we go through each node at the current level, we compare each node's value to this variable. If a node's value is higher, we update the variable. After checking all nodes at that level, this variable will hold the highest value for that level. We then save this maximum value and move on to the next level. This way, we find and record the largest value for each row of the tree.