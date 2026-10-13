class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums.sort()
        greatest = 0
        cur = 0
        print(nums)
        prevNum = float("inf")
        for num in nums:
            if num == prevNum+1:
                cur+=1
            elif num == prevNum:
                continue
            else:
                cur = 0
            prevNum = num
            if(cur > greatest):
                greatest = cur
        
        return greatest+1