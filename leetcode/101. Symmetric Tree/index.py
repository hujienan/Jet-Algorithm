# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val == right.val) and check(left.left, right.right) and check(left.right, right.left)
        return check(root, root)
            
            
             