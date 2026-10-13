class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        res = []
        while(k>0):
            highest = -1
            index = 0
            for num in hashtable:
                if (hashtable[num] > highest):
                    highest = hashtable[num]
                    index = num
            k-=1
            res.append(index)
            hashtable.pop(index)
        
        return res
