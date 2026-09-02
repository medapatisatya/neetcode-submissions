class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num] += 1
        
        # heap
        # import heapq
        # heap = []
        # heapq.heapify(heap)
        # for nk in nums_map:
        #     heapq.heappush(heap, [nums_map[nk], nk])

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return [x[1] for x in heap]

        # Bucket indexing since range lenght of arrary can be upto 10^4
        
        buc = [list() for i in range(len(nums))] # Index is freq and numbers are values of list.
        for nk in nums_map:
            buc[nums_map[nk]-1].append(nk)
        # Getting the result
        res = []
        for ind in buc[::-1]:
            for val in ind:
                res.append(val)
                if len(res) == k: return res





