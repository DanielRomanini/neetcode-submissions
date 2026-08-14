class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlength = len(nums) * 2
        length = len(nums)
        arr = [0] * newlength
        for i in range(length):
            arr[i] = nums[i]
            arr[i+length] = nums[i]
            
        return arr