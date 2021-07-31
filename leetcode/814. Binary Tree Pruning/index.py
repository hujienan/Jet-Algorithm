# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def recur(node):
            if not node:
                return None
            node.left = recur(node.left)
            node.right = recur(node.right)
            if node.val == 1 or node.right or node.left:
                return node
            return None
        return recur(root)


container = []


def toList(root: TreeNode):
    if not root:
        container.append(None)
        return
    container.append(root.val)
    if root.left or root.right:
        toList(root.left)
        toList(root.right)


solution = Solution()
# Testcase [1,null,0,0,1]
root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
# printTree(root)
toList(root)
assert container == [1, None, 0, 0, 1], "Tree to list is wrong"
res = solution.pruneTree(root)
container = []
toList(res)
assert container == [1, None, 0, None, 1], "Pruned tree is wrong"
