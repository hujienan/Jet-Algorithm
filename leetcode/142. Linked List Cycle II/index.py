# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow1, slow2, fast = head, head, head
        while fast and fast.next:
            slow1 = slow1.next
            fast = fast.next.next
            if slow1 == fast:
                while slow1 != slow2:
                    slow1 = slow1.next
                    slow2 = slow2.next
                return slow1