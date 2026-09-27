class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        maxCur = 0
        maxSum = nums[0]
        while(L<=R):
            maxCur = max(nums[L],maxCur+nums[L])
            maxSum = max(maxSum,maxCur)
            L+=1
        
        return maxSum