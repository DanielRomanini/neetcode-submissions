class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least = 1 
        most = max(piles)
        res = most

        while (most >= least):
            k = int((most+least)/2)
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)
            
            if (hours <= h):
                res = min(res,k)
                most = k - 1
            else:
                least = k + 1
        
        return res
