class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        buy, mp = prices[0], 0
        for price in prices[1:]:
            if price < buy: buy = price
            else: mp = max(mp, price - buy)
        return mp