class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mostProfit = 0
        l = 0
        for r, price in enumerate(prices):
            if(price<prices[l]):
                l=r
            mostProfit = max(mostProfit,price-prices[l])
        
        return mostProfit
