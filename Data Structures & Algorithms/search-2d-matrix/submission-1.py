class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerL=0
        outerR=len(matrix)-1
        middle = 0

        while(outerR>=outerL):
            middle = int((outerL+outerR)/2)
            if (target<matrix[middle][0]):
                outerR = middle - 1
            elif(target>matrix[middle][len(matrix[middle])-1]):
                outerL = middle + 1
            else:
                break
        
        innerL = 0
        innerR = len(matrix[middle])-1
        while(innerR>=innerL):
            middle2 = int((innerL+innerR)/2)
            if(target<matrix[middle][middle2]):
                innerR = middle2-1
            elif(target>matrix[middle][middle2]):
                innerL = middle2+1
            else:
                return True
        
        return False