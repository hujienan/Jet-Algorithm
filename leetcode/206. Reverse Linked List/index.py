# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive way
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
        
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative way
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev, head = head, tmp
        return prev
