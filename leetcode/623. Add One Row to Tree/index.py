# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def t(node, d = 0):
            if not node:
                return
            if d + 1 == depth:
                left, right = node.left, node.right
                newLeft = TreeNode(val, left)
                newRight = TreeNode(val, None, right)
                node.left, node.right = newLeft, newRight
            t(node.left, d+1)
            t(node.right, d+1)
        
        dummy = TreeNode(-1, root)
        t(dummy)
        return dummy.left
                    