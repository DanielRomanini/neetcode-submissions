class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R= 0,len(prices)-1
        greatest = -1

        for i,num in enumerate(prices):
            temp = prices[i:]
            most = max(temp)
            if (most-num>greatest):
                greatest = most-num

        return greatest