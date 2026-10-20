class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(r>l):
            middle = (l+r)//2
            if(nums[middle]>nums[r]):
                l = middle + 1
            else:
                r = middle

        pivot = l
        def binary_search(left,right):
            while(right>=left):
                middle = (right+left)//2
                if(nums[middle]>target):
                    right = middle - 1
                elif nums[middle]<target:
                    left = middle + 1
                else:
                    return middle
            return -1
        
        result = binary_search(0,pivot-1)
        if result!=-1:
            return result
        return binary_search(pivot,len(nums)-1)