# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def t(node, nums = []):
            if not node:
                return
            if not node.left and not node.right:
                res.append("->".join(str(_) for _ in [*nums, node.val]))
                return
            t(node.left, [*nums, node.val])
            t(node.right, [*nums, node.val])
        t(root)
        return res