class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search

        #if number all the way to the left is bigger than number all the way to the right,
        #we want to search the right portion

        minimum = float("inf")

        l, r = 0, len(nums) - 1
        while(r>=l):
            middle = int((l+r)/2)
            if(nums[middle]>nums[r]):
                minimum = min(minimum,nums[r])
                l = middle + 1
            else:
                minimum = min(minimum,nums[middle])
                r = middle - 1
        
        return minimum
