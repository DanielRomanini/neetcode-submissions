class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L,R = 0,0
        queue = deque()

        while(R<len(nums)):
            queue.append(nums[R])
            if R-L <= k:
                temp = set(queue)
                if len(queue) != len(temp):
                    return True
            if R-L == k:
                L+=1
                queue.popleft()
            R+=1
        return False