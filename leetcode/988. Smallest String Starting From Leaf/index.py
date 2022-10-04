# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "~"
        def t(node, nums = []):
            if not node:
                return
            if not node.left and not node.right:
                path = nums[::]
                path.append(chr(node.val + 97))
                path.reverse()
                self.ans = min(self.ans, "".join(path))
                return
            t(node.left, [*nums, chr(node.val + 97)])
            t(node.right, [*nums, chr(node.val + 97)])
        t(root)
        return self.ans