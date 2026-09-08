class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashtable = {}
        if len(nums)==0:
            return 0


        smallest = nums[0]
        for num in nums:
            if num<smallest:
                smallest = num
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        res = []
        temp = []
        count = 0
        for num in hashtable:
            if(num-1 in hashtable):
                continue
            cur = num
            temp.append(cur)
            while(cur+1 in hashtable):
                cur = cur + 1
                temp.append(cur)
                #hashtable.pop(cur)
            if(len(temp) > len(res)):
                res = temp
            temp = []
        
        return len(res)


