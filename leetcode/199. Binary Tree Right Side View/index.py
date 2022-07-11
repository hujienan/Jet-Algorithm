# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def t(node, i):
            if not node:
                return
            if not len(res) > i:
                res.append(node.val)
            t(node.right, i + 1)
            t(node.left, i + 1)
        t(root, 0)
        return res
                