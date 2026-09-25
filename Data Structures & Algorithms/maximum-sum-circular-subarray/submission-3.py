class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = 0
        sumMax = nums[0]
        curMin = 0
        sumMin = nums[0]
        totSum = 0
        tempMax = 0
        tempMin = 0

        for num in nums:
            totSum += num

            curMin = min(num,curMin+num)
            sumMin = min(sumMin,curMin)

            curSum += num
            sumMax = max(sumMax,curSum)

            if(curSum<0):
                curSum = 0

        print(sumMax)

        if sumMax<0:
            return sumMax
        if totSum-sumMin > sumMax:
            return totSum-sumMin
        return sumMax
            
