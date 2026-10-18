class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       # print("A")
        first, last = 0, len(matrix)-1
        row = 0
        while(last >= first):
            middle = int((first+last)/2)
            print(first, last, middle)
            if(matrix[middle][0] > target):
                last = middle - 1
            elif(matrix[middle][len(matrix[middle])-1] < target):
                first = middle + 1
            else:
                row = middle
                break

        l, r = 0, len(matrix[row])-1
        print(row)

        while(r>=l):
            middle = int((r+l)/2)
            if (matrix[row][middle] < target):
                l = middle + 1
            elif (matrix[row][middle] > target):
                r = middle - 1
            else:
                print(row,middle)
                return True
        return False