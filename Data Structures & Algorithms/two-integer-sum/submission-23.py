class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i,num in enumerate(nums):
            hashset[num] = i

        for i,num in enumerate(nums):
            needed = target - num
            if needed in hashset and i != hashset[needed]:
                return [i,hashset[needed]]

        return []