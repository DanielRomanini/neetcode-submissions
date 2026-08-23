class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while(right>=left):
            k = int((right+left)/2)
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)
            
            if (hours > h):
                left = k + 1
            else:
                res = min(res,k)
                right = k - 1
            
        return res