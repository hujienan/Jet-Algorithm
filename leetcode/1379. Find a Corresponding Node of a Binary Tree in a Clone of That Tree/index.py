# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def t(node):
            if not node:
                return None
            if node.val == target.val:
                return node
            return t(node.left) or t(node.right)
        return t(cloned)