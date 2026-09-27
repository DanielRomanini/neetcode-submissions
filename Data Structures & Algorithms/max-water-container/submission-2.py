class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        most = 0
        while(R>L):
            most = max(most,min(heights[L],heights[R])*(R-L))
            if heights[L] > heights[R]:
                R-=1
            else:
                L+=1
        
        return most