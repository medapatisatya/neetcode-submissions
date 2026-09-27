# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, dummy = [], ListNode()
        temp = dummy
        
        for l in lists:
            if l:
                heapq.heappush(heap, l)
                    
            
        while heap:
            node = heapq.heappop(heap)

            dummy.next = node
            dummy = dummy.next

            if node.next:
                heapq.heappush(heap, node.next)
        return temp.next

            