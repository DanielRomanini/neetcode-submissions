class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if (len(nums) <= 1):
            return
        
        count = [0,0,0]
        for n in nums:
            count[n]+=1

        i=0
        temp = 0
        for n in range(len(count)):
            while True:
                if(temp>=count[n]):
                    break
                nums[i] = n
                i+=1
                temp+=1
            temp = 0

        
        """
        Do not return anything, modify nums in-place instead.
        """
        