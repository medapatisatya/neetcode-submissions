class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: Get freq, then sort and send k keys.
        # freq = defaultdict(int)
        # for num in nums:
        #     freq[num] += 1
        
        # freqs = list(map(list, freq.items()))
        # freqs.sort(key=lambda x: -x[1]) # we don't need to sort all elements.
        # return [x[0] for x in freqs[:k]]

        # Approach 2: Bucket sort (we dont actually sort anything here).
        # Frequecny Buckets.
        # freq = defaultdict(int)
        # for num in nums: freq[num] += 1

        # freqs_bucket = [list() for i in range(len(nums))]

        # for num in freq:
        #     freqs_bucket[freq[num]-1].append(num)
        
        # res = []
        # for freqs in freqs_bucket[::-1]:
        #     for num in freqs:
        #         res.append(num)
        #         if len(res) == k: return res

        # Approach 3: Heap: Need to know more about heaps.
        # Using python heap but need to create my own heap ds next time.
        freq = defaultdict(int)
        for num in nums: freq[num] += 1
        freqs = list(zip(freq.values(), freq.keys()))

        # dont need to heapify first as it is getting costly operation
        # insertion and retrival.
        # heapq.heapify(freqs)
        # while len(freqs) > k:
        #     heapq.heappop(freqs)

        # heapify one by one.
        heap = []
        for item in freqs:
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]