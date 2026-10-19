class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        bananas = float("inf")
        while(r>=l):
            middle = int((l+r)/2)
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(pile/middle)
            if(hoursTaken>h):
                l = middle + 1
            elif (hoursTaken<=h):
                r = middle - 1
                bananas = min(bananas,middle)
        
        return bananas