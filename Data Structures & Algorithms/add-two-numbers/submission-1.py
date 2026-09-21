# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s, c = 0, 0
        temp = dummy = ListNode()
        while l1 and l2:
            s = l1.val + l2.val + c
            s, c = s%10, s//10
            temp.next = ListNode(s)
            l1, l2, temp = l1.next, l2.next, temp.next
        l1 = l1 or l2
        while l1:
            s = l1.val + c
            s, c = s%10, s//10
            temp.next = ListNode(s)
            temp, l1 = temp.next, l1.next
        if c:
            temp.next = ListNode(c)
        return dummy.next