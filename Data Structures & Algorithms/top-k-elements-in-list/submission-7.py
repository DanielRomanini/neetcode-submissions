class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num]+=1
        
        temp = []
        key = 0
        while(k>0):
            highest = -1
            for i in hashtable:
                if hashtable[i] > highest:
                    highest = hashtable[i]
                    key = i
            temp.append(key)
            k-=1
            hashtable[key] = -1
        return temp