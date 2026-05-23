class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        maxProfit = 0
        
        for end in range(1, len(prices)):
            currentProfit = prices[end] - prices[start]
            maxProfit = max(maxProfit, currentProfit)

            if prices[end] < prices[start]:
                start = end
        
        return maxProfit