class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        for num in nums:
            if num!=0:
                product*=num
            else:
                zeroCount+=1
        
        for i in range(len(nums)):
            if zeroCount>1:
                nums[i] = 0
            else:
                if zeroCount == 1:
                    if nums[i] == 0:
                        nums[i] = product
                    else:
                        nums[i] = 0
                else:
                    nums[i] = int(product/nums[i])
        
        return nums