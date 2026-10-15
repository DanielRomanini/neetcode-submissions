class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        most = 0
        l, r = 0, 1
        while(r<len(prices)):
            if (prices[r]<lowest):
                lowest = prices[r]
                l = r
                r += 1
                continue
            
            most = max(most,prices[r]-lowest)
            r+=1
        
        return most