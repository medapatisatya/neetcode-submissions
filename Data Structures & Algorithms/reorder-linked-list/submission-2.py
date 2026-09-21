# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getParts(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None
        return head, part2
    
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def merge(self, part1, part2):
        dummy = ListNode()
        temp = dummy
        while part1 and part2:
            temp.next = part1
            part1 = part1.next
            temp = temp.next
            
            temp.next = part2
            part2 = part2.next
            temp = temp.next
        
        temp.next = part1 or part2
        return dummy.next
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        part1, part2 = self.getParts(head)
        part2 = self.reverse(part2)
        head = self.merge(part1, part2)