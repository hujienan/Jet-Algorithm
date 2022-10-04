# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def t(node, total = 0):
            if not node:
                return False
            if not node.left and not node.right and node.val + total == targetSum:
                return True
            return t(node.left, node.val+total) or t(node.right, node.val+total)
        return t(root)