# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        
        def reverse(node):
            if not node or not node.next:
                return node
            last = reverse(node.next)
            node.next.next = node
            node.next = None
            return last
        
        r = reverse(slow)
        maxSum = 0
        while r:
            maxSum = max(maxSum, r.val + head.val)
            r = r.next
            head = head.next
        return maxSum