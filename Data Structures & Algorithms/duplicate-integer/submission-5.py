class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1

        
        return not (len(hashmap) == len(nums))