class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bananas = max(piles)
        hoursTaken = 0
        l, r = 1, bananas

        while(r>=l):
            hoursTaken = 0
            middle = int((l+r)/2)
            for pile in piles:
                hoursTaken += math.ceil(pile/middle)
            print(l, r, middle,hoursTaken, bananas)
            
            if(hoursTaken>h):
                l = middle + 1
            if(hoursTaken<=h):
                r = middle - 1
                bananas = min(bananas,middle)
            
        
        return bananas