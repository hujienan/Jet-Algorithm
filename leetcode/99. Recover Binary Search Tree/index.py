# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        values = []
        def t(root):
            if root:
                t(root.left)
                values.append(root.val)
                t(root.right)
        t(root)
        values.sort()
        wrongNodes = []
        def check(root):
            if root:
                check(root.left)
                value = values.pop(0)
                if root.val != value:
                    wrongNodes.append(root)
                check(root.right)
        check(root)
        wrongNodes[0].val, wrongNodes[1].val = wrongNodes[1].val, wrongNodes[0].val
        
        