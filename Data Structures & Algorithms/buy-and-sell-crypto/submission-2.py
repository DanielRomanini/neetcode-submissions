class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        leastInWindow = prices[0]
        res = float("-inf")

        for r in range(len(prices)):
            res = max(res,prices[r]-leastInWindow)
            if prices[r] <leastInWindow:
                l = r
                leastInWindow = prices[r]

        if res<=0:
            return 0
        return res
