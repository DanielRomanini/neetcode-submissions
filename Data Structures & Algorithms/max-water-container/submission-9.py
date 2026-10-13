class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = -1
        l, r = 0, len(heights)-1
        while(r>l):
            cur = min(heights[l],heights[r])
            temp = cur * (r-l)
           #w print(cur, temp)
            if temp>most:
                most = temp
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return most