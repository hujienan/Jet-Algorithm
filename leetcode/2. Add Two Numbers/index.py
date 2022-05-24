# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        dummy = res
        carry = 0
        while carry or l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry, v =  divmod(v1 + v2 + carry, 10)
            dummy.next = ListNode(v)
            dummy = dummy.next
        return res.next
        