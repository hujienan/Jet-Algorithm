# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def t(node):
            if not node:
                return 0
            res = 0
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                else:
                    res += t(node.left)
            res += t(node.right)
            return res

        return t(root)
