# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 0 not covered
        # 1 camera
        # 2 covered
        self.res = 0
        def t(node):
            if not node:
                return 2
            l = t(node.left)
            r = t(node.right)
            if not l or not r:
                self.res += 1
                return 1
            if l == 2 and r == 2:
                return 0
            else:
                return 2
        
        state = t(root)
        if not state:
            self.res += 1            
        return self.res
            