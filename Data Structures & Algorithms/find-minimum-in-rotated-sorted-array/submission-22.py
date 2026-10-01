class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        element = nums[0]

        while(r>=l):
            m = int((r+l)/2)
            if nums[r]>nums[l]:
                return min(element,nums[l])
            element = min(element,nums[m])
            if(nums[m]>=nums[l]):
                l = m+1
            else:
                r = m - 1
            
            
            
        
        return element