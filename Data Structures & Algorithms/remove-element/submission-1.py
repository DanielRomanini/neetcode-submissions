class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                k+=1
        for i in range(len(nums)):
            if(nums[i] == val):
                j = i
                if((j+1)<len(nums)):
                    j+=1
                while((j+1)<len(nums) and nums[j] == val):
                    j+=1
                nums[i] = nums[j]
                nums[j] = val
        return len(nums)-k