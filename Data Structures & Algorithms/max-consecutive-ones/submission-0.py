class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        for i in range(len(nums)):
            if (nums[i] == 1):
                temp += 1
                if (temp>count):
                    count = temp
            else:
                temp = 0
        return count

        