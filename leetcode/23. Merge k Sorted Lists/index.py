# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        temp = []
        for i in range(length):
            cur = lists[i]
            while cur:
                temp.append(cur.val)
                cur = cur.next
        temp.sort()
        dummy = ListNode()
        test = dummy
        for i in range(len(temp)):
            test.next = ListNode(temp[i])
            test = test.next
        return dummy.next