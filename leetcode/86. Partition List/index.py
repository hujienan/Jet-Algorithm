# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1, head2 = ListNode(), ListNode()
        dummy1, dummy2 = head1, head2
        while head:
            if head.val < x:
                dummy1.next = head
                dummy1 = dummy1.next
            else:
                dummy2.next = head
                dummy2 = dummy2.next
            head = head.next
        dummy2.next = None
        dummy1.next = head2.next
        return head1.next