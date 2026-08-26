class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = []
        first = 0
        second = 0
        while first<m and second<n:
            if nums1[first] < nums2[second]:
                temp.append(nums1[first])
                first+=1
            else:
                temp.append(nums2[second])
                second+=1
        if first < m:
            for i in range(first,m):
                temp.append(nums1[i])
            
        elif second<n:
            for i in range(second,n):
                temp.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = temp[i]
        


        