class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = [0] * len(prices)
        
        mini[0] = prices[0]
        for i in range(1, len(prices)):
            mini[i] = min(prices[i], mini[i-1])
        
        maxi = 0
        for i in range(1, len(prices)):
            maxi = max(maxi, prices[i]-mini[i-1])

        return maxi
        