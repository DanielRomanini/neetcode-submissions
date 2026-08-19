class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        
        while (L<=R):
            middle = int((R+L)/2)
            print(middle)
            if(nums[middle]>target):
                R=middle-1
            elif (nums[middle]<target):
                L = middle + 1
            else:
                return middle

        return -1