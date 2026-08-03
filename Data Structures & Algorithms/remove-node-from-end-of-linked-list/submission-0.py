# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterate and find length
        ns, length, temp = 0, 0, head
        while temp:
            length += 1
            temp = temp.next
        ns = length - n

        if ns == 0:
            return head.next
        else:
            prev, count, temp = None, 0, head
            while temp:
                if count == ns:
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next
                count += 1
        return head


