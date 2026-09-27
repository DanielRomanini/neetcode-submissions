class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L,R = 0,0
        temp = set()
        if k == 0:
            return False

        while(R<len(nums)):
            if R-L <= k:
                if nums[R] in temp:
                    return True
            if R-L == k:
                temp.remove(nums[L])
                L+=1
               # print(temp,nums[L])
            temp.add(nums[R])
            R+=1
        return False