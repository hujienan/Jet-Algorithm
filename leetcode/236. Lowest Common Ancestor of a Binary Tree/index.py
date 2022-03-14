# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node):
            if not node:
                return False
            left = recur(node.left)
            right = recur(node.right)
            mid = node == p or node == q
            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
        recur(root)
        return self.ans

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        a = set()
        while p:
            a.add(p)
            p = parent[p]
        while q not in a:
            q = parent[q]
        return q
