class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index

        final = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap and i != hashmap[diff]:
                final.append(i)
                final.append(hashmap[diff])
                break
        return final