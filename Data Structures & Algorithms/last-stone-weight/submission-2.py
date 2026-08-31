class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        count = 0
        length = len(stones)
        while(count<length-1):
            first = heapq.heappop(stones) #-2
            second = heapq.heappop(stones) #-1
            if(second == first):
                print("AAAA")
                count+=2
            else:
                print(first,second)
                heapq.heappush(stones,first-second)
                count+=1
        if(count==length):
            return 0
        if(len(stones)>1):
            heapq.heappop(stones)
        return -heapq.heappop(stones)
            