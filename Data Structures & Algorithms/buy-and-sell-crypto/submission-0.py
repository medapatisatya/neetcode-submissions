class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, prices[0]
        for i in range(len(prices) - 1):
            if prices[i+1] < min_price: min_price = prices[i+1]
            else: max_profit = max(max_profit, prices[i+1]-min_price)
        return max_profit