# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from typing import Optional


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def t(node):
            if not node:
                return [True, math.inf, -math.inf, 0]
            is_left_bst, left_low, left_high, left_sum = t(node.left)
            is_right_bst, right_low, right_high, right_sum = t(node.right)
            cur_sum = node.val
            is_bst = is_left_bst and is_right_bst and node.val > left_high and node.val < right_low
            if is_bst:
                cur_sum = node.val + left_sum + right_sum
                self.res = max(self.res, cur_sum)
            return [is_bst, min(node.val, left_low, right_low), max(node.val, left_high, right_high), cur_sum]
        t(root)
        return self.res
