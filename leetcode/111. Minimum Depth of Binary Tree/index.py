# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def t(node):
            if not node:
                return 0
            l = t(node.left)
            r = t(node.right)
            if l and r:
                cur = min(l, r)
            elif l:
                cur = l
            else:
                cur = r
            return 1 + cur
        return t(root)