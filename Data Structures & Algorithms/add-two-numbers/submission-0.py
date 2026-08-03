# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c, s = 0, 0
        dummy = head = ListNode()

        while l1 and l2:
            s = l1.val + l2.val + c
            val, c = s % 10, s // 10
            head.next = ListNode(val)
            head = head.next
            l1, l2 = l1.next, l2.next

        while l1:
            s = l1.val + c
            val, c = s % 10, s // 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
        
        while l2:
            s = l2.val + c
            val, c = s % 10, s // 10
            head.next = ListNode(val)
            head = head.next
            l2 = l2.next
        
        if c:
            head.next = ListNode(c)
        
        return dummy.next