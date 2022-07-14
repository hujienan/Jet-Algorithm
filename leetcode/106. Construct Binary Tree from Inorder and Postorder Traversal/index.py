# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node_val = postorder.pop()
        node = TreeNode(node_val)
        index_in_inorder = inorder.index(node_val)
        left_inorder = inorder[:index_in_inorder]
        right_inorder = inorder[index_in_inorder+1:]
        node.right = self.buildTree(right_inorder, postorder) if len(right_inorder) > 0 else None
        node.left = self.buildTree(left_inorder, postorder) if len(left_inorder) > 0 else None
        return node