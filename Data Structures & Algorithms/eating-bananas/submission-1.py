import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHours(k, piles):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours
        
        l,r = 1, max(piles)
        mk = r

        while l <= r:
            m = (l+r)//2
            mh = findHours(m, piles)
            if mh <= h:
                mk = min(mk, m)
                r = m - 1
            else:
                l = m + 1
        
        return mk