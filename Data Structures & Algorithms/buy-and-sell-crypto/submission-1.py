class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #when we see an element smaller than current start
        #that now becomes our start, then we keep checking for max profit 
        start = 0
        maxProfit = 0
        currentProfit = 0

        for end in range(len(prices)):
            currentProfit = prices[end] - prices[start]
            maxProfit = max(currentProfit, maxProfit)

            if prices[end] < prices[start]:
                start = end
        
        return maxProfit 
        