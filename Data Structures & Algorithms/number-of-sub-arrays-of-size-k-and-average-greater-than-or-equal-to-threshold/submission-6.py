class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, R = 0, 0
        count,curSum = 0,0
        while(R<len(arr)):
            curSum += arr[R]
            if R-L+1 == k:
                if curSum/k>=threshold:
                    count+=1
                curSum-=arr[L]
                L+=1
            R+=1
        return count                    

