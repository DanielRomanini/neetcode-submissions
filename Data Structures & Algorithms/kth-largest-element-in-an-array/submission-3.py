class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapq.heapify(arr)

        while(k>0):
            cur = heapq.heappop(arr)
            k-=1
        
        return -cur