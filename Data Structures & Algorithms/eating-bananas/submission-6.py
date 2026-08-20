class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while(right>=left):
            middle = int((left+right)/2)
            hours = 0 
            for p in piles:
                hours+= math.ceil(p/middle)

            if (hours<=h):
                res = min(res,middle)
                right = middle - 1
            else:
                left = middle + 1
        return res



            