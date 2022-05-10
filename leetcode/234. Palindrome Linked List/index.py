# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        c = []
        dummy = head
        while dummy:
            c.append(dummy.val)
            dummy = dummy.next
        c1 = list(reversed(c))
        return c == c1