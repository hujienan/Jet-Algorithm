# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def dfs(n, target, path):
            if not n:
                return False
            if n.val == target:
                return True
            path.append("L")
            res = dfs(n.left, target, path)
            if res:
                return path
            path.pop()
            path.append("R")
            res = dfs(n.right, target, path)
            if res:
                return path
            path.pop()
            return False

        s, d = deque(), deque()
        dfs(root, startValue, s)
        dfs(root, destValue, d)
        while len(s) and len(d) and s[0] == d[0]:
            s.popleft()
            d.popleft()
        return "".join("U" * len(s)) + "".join(d)
