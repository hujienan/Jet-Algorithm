# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        dummy = head
        while dummy:
            q.append(ListNode(dummy.val))
            dummy = dummy.next
        dummy = head
        if q:
            q.popleft()
        while q:
            r = q.pop()
            dummy.next = r
            dummy = dummy.next
            if q:
                l = q.popleft()
                dummy.next = l
                dummy = dummy.next
        
            
            
        