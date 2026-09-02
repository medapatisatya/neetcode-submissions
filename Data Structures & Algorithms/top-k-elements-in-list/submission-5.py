class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num] += 1
        
        # heap
        import heapq
        heap = []
        heapq.heapify(heap)
        for nk in nums_map:
            heapq.heappush(heap, [nums_map[nk], nk])

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]

        