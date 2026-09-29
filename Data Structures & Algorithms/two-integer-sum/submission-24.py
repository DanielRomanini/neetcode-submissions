class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for j in range(len(nums)):
            needed = target - nums[j]
            if needed in hashmap and j!= hashmap[needed]:
                return [j,hashmap[needed]]