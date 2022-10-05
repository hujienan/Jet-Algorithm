# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def t(node, nums = []):
            if not node:
                return
            if not node.left and not node.right:
                path = [*nums, node.val]
                s = "".join(str(_) for _ in path)
                self.res += int(s)
                return
            t(node.left, [*nums, node.val])
            t(node.right, [*nums, node.val])
        t(root)
        return self.res