# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newh, ohead, nhead, length, temp, new_head = None, None, None, 0, head, None

        # For finding length
        while temp:
            length += 1 
            temp = temp.next
        
        for i in range(length // k):
            j, prev = k, None

            if i > 0: ohead = nhead
            nhead = head

            while j:
                j -= 1
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            if not new_head: new_head = prev
            if ohead: ohead.next = prev
        if new_head: nhead.next = head
        return new_head or head
