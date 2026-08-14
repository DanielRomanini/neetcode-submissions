class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlength = len(nums) * 2
        length = len(nums)
        arr = []
        for i in range(newlength):
            if(i<length):
                arr.append(nums[i])
            else:
                arr.append(nums[i-length])
            
        return arr