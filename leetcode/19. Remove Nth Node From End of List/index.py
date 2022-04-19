# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy = ListNode()
        # dummy.next = head
        # test = head
        # length = 0
        # while test:
        #     length += 1
        #     test = test.next
        # length -= n
        # test = dummy
        # while length > 0:
        #     length -= 1
        #     test = test.next
        # test.next = test.next.next
        # return dummy.next
        dummy = ListNode(0, head)
        p1 = p2 = dummy
        for _ in range(n+1):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
                
        
        