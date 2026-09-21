# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        rem = length - n
        if rem == 0: return head.next
        prev, temp = None, head
        while rem:
            rem -= 1
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        return head