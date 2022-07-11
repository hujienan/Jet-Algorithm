# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(node):
            midPrev = None
            while node and node.next:
                if not midPrev:
                    midPrev = node
                else:
                    midPrev = midPrev.next
                node = node.next.next
            mid = midPrev.next
            midPrev.next = None
            return mid
        def merge(l1, l2):
            dummy = ListNode()
            p = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    p.next = l2
                    l2 = l2.next
                else:
                    p.next = l1
                    l1 = l1.next
                p = p.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next
        if not head or not head.next:
            return head
        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)