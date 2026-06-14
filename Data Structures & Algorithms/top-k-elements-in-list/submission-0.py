class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: Get freq, then sort and send k keys.
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        freqs = list(map(list, freq.items()))
        freqs.sort(key=lambda x: -x[1])
        return [x[0] for x in freqs[:k]]