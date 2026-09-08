class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num]+=1

        

        res = []
        while(k>0):
            greatest = -1
            greatestIndex = -1
            for num in hashtable:
                if hashtable[num] > greatest:
                    greatest = hashtable[num]
                    greatestIndex = num
            res.append(greatestIndex)
            hashtable[greatestIndex] = -2
            k-=1
        
        return res
