# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findMid(self, head: Optional[ListNode]) -> ListNode:
        slow, fast, prev = head, head, None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        second = None
        if fast:
            second = slow.next
            slow.next = None
        else:
            prev.next = None
            second = slow
        
        return second
    
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    
    def mergeList(self, l1, l2):
        temp = ListNode()
        while l1 and l2:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and not head.next: return None
        second = self.findMid(head)
        second = self.reverse(second)
        self.mergeList(head, second)
