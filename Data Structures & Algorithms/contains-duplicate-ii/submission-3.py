class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        if k == 0:
            return False
        window.add(nums[0])
        if len(nums) <= 1:
            return False
        L=0
        R=1
        while R<len(nums):
            if abs(L-R) > k:
                window.remove(nums[L])
                L+=1
                window.add(nums[L])
            if nums[R] in window:
                return True
            window.add(nums[R])
            R+=1
        return False