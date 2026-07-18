import math
class Solution:
    def get_hours(self, mid, piles):
        total = 0
        for i in piles:
            total += math.ceil(i/mid)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high, m = 1, max(piles), max(piles)
        while low <= high:
            mid = (low + high) // 2
            hours = self.get_hours(mid, piles)
            if hours <= h:
                m = min(m, mid)
                high = mid - 1
            else:
                low = mid + 1
        return m