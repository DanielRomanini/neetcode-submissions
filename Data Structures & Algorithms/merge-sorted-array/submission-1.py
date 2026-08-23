class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = []
        first = 0
        second = 0

        while(first != m and second != n):
            if(nums1[first]<nums2[second]):
                arr.append(nums1[first])
                first+=1
            else:
                arr.append(nums2[second])
                second+=1
            
        while(first!=m):
            arr.append(nums1[first])
            first+=1
        while(second!=n):
            arr.append(nums2[second])
            second+=1
        
        for i in range(len(arr)):
            nums1[i] = arr[i]
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        