class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerL = 0
        outerR = len(matrix)-1

        while(outerL<=outerR):
            print("outer loop")
            outerM = int((outerL+outerR)/2)

            if(target<matrix[outerM][0]):
                outerR = outerM-1
            elif(target>matrix[outerM][len(matrix[outerM])-1]):
                outerL = outerM+1
            else:
                break

            if(outerL>outerR):
                return False
                
        innerL = 0
        innerR = len(matrix[outerM])-1

        while(innerL<=innerR):
            print("iiner llo")
            innerM = int((innerL+innerR)/2)
            if(target>matrix[outerM][innerM]):
                innerL = innerM + 1
            elif(target<matrix[outerM][innerM]):
                innerR = innerM - 1
            else:
                return True

        return False



