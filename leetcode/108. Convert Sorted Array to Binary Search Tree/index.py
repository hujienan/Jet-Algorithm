# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def t(nums):
            if not nums:
                return None
            length = len(nums)
            mid = length // 2
            node = TreeNode(nums[mid])
            node.left = t(nums[:mid])
            node.right = t(nums[mid+1:])
            return node
        return t(nums)
            