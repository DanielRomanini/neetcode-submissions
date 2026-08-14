class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = 0
        for i in range(len(arr)-1):
            temp = 0
            for j in range(i+1, len(arr)):
                if (arr[j]>temp):
                    temp = arr[j]
            arr[i] = temp
        arr[len(arr)-1] = -1
        return arr