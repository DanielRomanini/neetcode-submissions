class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashtable = {}
        res = []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1,len(nums)-1

            while(r>l):
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    temp = [nums[i],nums[l],nums[r]]
                    temp.sort()
                    if(tuple(temp) not in hashtable):
                        hashtable[tuple(temp)] = 1
                    l+=1
        for num in hashtable:
            res.append(num)
        
        return res