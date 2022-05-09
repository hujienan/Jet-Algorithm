# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        w, r = divmod(length, k)
        res = []
        cur = head
        for i in range(k):
            c = cur
            times = w + 1 if i < r else w
            for _ in range(times - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            res.append(c)
        return res