class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                k+=1
                nums[i] = None
        for i in range(len(nums)):
            if(nums[i] == None):
                j = i
                while(j<len(nums)-1 and nums[j]==None):
                    j+=1
                nums[i] = nums[j]
                nums[j] = None
        return len(nums)-k