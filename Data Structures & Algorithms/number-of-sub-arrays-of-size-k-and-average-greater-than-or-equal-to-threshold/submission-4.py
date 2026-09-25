class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L=0
        R=0
        counter = 0
        stack = deque()
       # stack.append(arr[0])
        tot = 0

        while(R<len(arr)):

            if R-L+1>k:
                tot -= stack.popleft()
                L+=1

            tot+=arr[R]
            stack.append(arr[R])

            if R-L+1 == k:
                if tot/k >= threshold:
                    counter+=1

            R+=1
        
        return counter
