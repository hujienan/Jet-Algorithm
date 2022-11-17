# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDepth(self, node):
            if not node:
                return 0
            return self.findDepth(node.left) + 1
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.findDepth(root.left)
        r = self.findDepth(root.right)
        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2 ** r