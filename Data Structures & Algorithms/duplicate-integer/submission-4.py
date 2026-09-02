class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        if (len(hashMap)!=(len(nums))):
            return True
        return False