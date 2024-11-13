# max-depth.py

'''

Given:
    - Root of binary tree

Return:
    - Maximum depth

Concept:
    - Binary tree's max depth is th enumber of nodes along the longest path from the root to the farthest leaf node

'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time, O(n) space (due to stack frames being proportional to every node)
# Used preorder traversal root -> left -> right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case leaf
        if not root:
            return 0

        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        
        return max(left, right)