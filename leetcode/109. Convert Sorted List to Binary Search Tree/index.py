# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        dummy = head
        while dummy:
            val = dummy.val
            nums.append(val)
            dummy = dummy.next
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