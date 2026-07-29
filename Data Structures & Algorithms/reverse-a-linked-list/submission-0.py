# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        prev = None
        while head and head.next:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        if head:
            head.next = prev
        
        return head