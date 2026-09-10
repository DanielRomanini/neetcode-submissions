class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i 

        temp = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in hashtable and i!=hashtable[diff]):
                temp.append(i)
                temp.append(hashtable[diff])
                break
        
        temp.sort()
        return temp
                