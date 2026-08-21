class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bottom = 1
        top = max(piles)
        res = top

        while(top>=bottom):
            middle = int((top+bottom)/2)
            hours = 0

            for p in piles:
                hours += math.ceil(p/middle)
            if(hours<=h):
                res = min(res,middle)
                top = middle - 1

            else:
                bottom = middle + 1

        return res