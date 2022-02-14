# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def t(n):
            if not n:
                return 0
            return 1 + max(t(n.right), t(n.left))
        return t(root)