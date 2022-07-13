# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def t(node, level):
            if not node:
                return
            dic[level].append(node.val)
            t(node.left, level + 1)
            t(node.right, level + 1)
        t(root, 0)
        return dic.values()
            