# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def t(node, total = 0, nums = []):
            if not node:
                return
            if not node.left and not node.right and node.val + total == targetSum:
                nums.append(node.val)
                res.append(nums)
                return
            t(node.left, total + node.val, [*nums, node.val] )
            t(node.right, total + node.val, [*nums, node.val])
        
        t(root)
        return res