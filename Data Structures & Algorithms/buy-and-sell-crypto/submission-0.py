class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R= 0,len(prices)-1
        greatest = -1

        for i,num in enumerate(prices):
            for num2 in range(i,len(prices)):
                if (prices[num2]-num > greatest):
                    greatest = prices[num2]-num

        return greatest
                    