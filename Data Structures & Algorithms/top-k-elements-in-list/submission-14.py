class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1

        
        arr = []        
        greatest = 0
        frequency = 0
        for i in range(k):
            for num in hashtable:
                if hashtable[num] > frequency:
                    frequency = hashtable[num]
                    greatest = num
            arr.append(greatest)
            hashtable[greatest] = -1
            greatest = 0
            frequency = 0
        
        return arr