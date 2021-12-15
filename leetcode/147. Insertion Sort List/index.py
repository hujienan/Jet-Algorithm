# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = head
        while prev:
            dumdum = dummy
            while dumdum.next and dumdum.next.val < prev.val:
                dumdum = dumdum.next
            temp, dumdum.next = dumdum.next, prev
            prev = prev.next
            dumdum.next.next = temp
        return dummy.next
