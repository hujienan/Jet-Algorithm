# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        root_val = preorder[0]
        root = TreeNode(val=root_val)
        index_in_inorder = inorder.index(root_val)
        left_inorder = inorder[:index_in_inorder]
        right_inorder = inorder[index_in_inorder+1:]
        preorder.pop(0)
        root.left = self.buildTree(preorder, left_inorder) if len(left_inorder) > 0 else None
        root.right = self.buildTree(preorder, right_inorder) if len(right_inorder) > 0 else None
        return root

solution = Solution()
res = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])