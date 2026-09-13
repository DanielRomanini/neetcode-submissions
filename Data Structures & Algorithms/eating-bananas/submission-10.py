class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = max(piles)
        least = 1

        works = most

        while(most>=least):
            middle = int((most+least)/2) #k
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/middle)
            
            if(hours<=h):
                works = middle
                most = middle - 1
            else:
                least = middle + 1
        
        return works