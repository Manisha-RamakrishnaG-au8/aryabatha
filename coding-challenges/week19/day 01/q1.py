class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        sell = 0
        for i in range(len(prices)-1,-1,-1):
            sell = max(sell, prices[i])
            result = max(result, sell - prices[i])
        return result