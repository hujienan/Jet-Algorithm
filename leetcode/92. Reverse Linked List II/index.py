# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iterative way
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prevLeft, cur = dummy, head
        for _ in range(left - 1):
            prevLeft, cur = cur, cur.next
        
        prev = None
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        prevLeft.next.next = cur
        prevLeft.next = prev
        return dummy.next
    # recursive way
    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        suc = None
        def reverseN(head, n):
            nonlocal suc
            if n == 1:
                suc = head.next
                return head
            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = suc
            return last
        def reverseB(head, m, n):
            if m == 1:
                return reverseN(head, n - m + 1)
            head.next =  reverseB(head.next, m - 1, n - 1)
            return head
        return reverseB(head, left, right)
