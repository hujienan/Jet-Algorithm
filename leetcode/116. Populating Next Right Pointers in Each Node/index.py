"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs
        if not root:
            return root
        q = deque([root])
        while q:
            temp = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    node.next = temp
                    temp = node
                    q.append(node.right)
                    q.append(node.left)
        return root
    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # recursive
        def t(node):
            if not node:
                return
            if node.left:
                node.left.next = node.right
            if node.next:
                if node.right:
                    node.right.next = node.next.left
            t(node.right)
            t(node.left)
        t(root)
        return root
            
                    
                    