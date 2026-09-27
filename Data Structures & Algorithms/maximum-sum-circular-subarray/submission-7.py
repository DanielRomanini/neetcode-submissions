class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        minCur = 999999999999
        maxSum = nums[0]
        maxCur = -99999999999
        tot = 0
        R = 0

        posPresent = 0
        
        while(R<len(nums)):
            if(nums[R]>0):
                posPresent = 1
            tot += nums[R]

            maxCur = max(nums[R],nums[R]+maxCur)
            maxSum = max(maxSum,maxCur)
            print(minCur)
            minCur = min(nums[R],minCur + nums[R])
            minSum = min(minSum,minCur)
            print("A", minSum)
            R+=1
        
        if(tot-minSum > maxSum and posPresent==1):
            print("!")
            return tot-minSum
        return maxSum


