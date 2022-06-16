# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        # DFS
        def t(node):
            if not node:
                return 0
            l = t(node.left)
            r = t(node.right)
            if l and r:
                cur = min(l, r)
            elif l:
                cur = l
            else:
                cur = r
            return 1 + cur
        return t(root)
    
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        q = deque([root])
        depth = 1
        while q:
            length = len(q)
            for _ in range(length):
                n = q.popleft()
                if not n.left and not n.right:
                    return depth
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            depth += 1
        return depth