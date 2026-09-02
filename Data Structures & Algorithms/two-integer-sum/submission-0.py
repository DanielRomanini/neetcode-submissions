class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for ind,num in enumerate(nums):
            hashMap[num] = ind
        
        for ind,num in enumerate(nums):
            diff = target - num
            if (diff in hashMap and ind!=hashMap[diff]):
                arr = [ind,hashMap[diff]]
                break
        return arr

        