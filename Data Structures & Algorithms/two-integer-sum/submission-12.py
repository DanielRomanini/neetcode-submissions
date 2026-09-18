class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        arr = []
        for i in range(len(nums)):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = i
            
        for i in range(len(nums)):
            needed = target - nums[i]
            if(needed in hashtable and i!=hashtable[needed]):
                arr = [i,hashtable[needed]]
                
        arr.sort()
        return arr