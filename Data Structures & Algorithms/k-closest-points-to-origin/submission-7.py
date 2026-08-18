import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if (len(points)<=1):
            return points

        arr = []
        arr2 = []
        for i in range(len(points)):
            temp = []
            temp.append(math.sqrt((points[i][0])**2 + (points[i][1])**2))
            temp.append(i)
            arr.append(temp)
            arr2.append(math.sqrt((points[i][0])**2 + (points[i][1])**2))

        length = len(arr)-1
        self.quickSort(arr2,0,length)

        count = 0
        index = 0
        indexes = []
        while(k>0):
            for row in arr:
                #print(arr2[count],row[0])
                if (arr2[count] == row[0]):
                    indexes.append(row[1])
                    count+=1
                    k-=1
                if(k<1):
                    break


        
        final = []
        for i in indexes:
            final.append(points[i])
        return final

            
        
    def quickSort(self,arr: List[int], start, end):
        if (end - start + 1)<=1:
            return arr
        
        pivot = arr[end]
        left = start
        for i in range(start, len(arr)):
            if (arr[i]<pivot):
                temp = arr[left]  
                arr[left] = arr[i]
                arr[i] = temp
                left+=1
        
        arr[end] = arr[left]
        arr[left] = pivot        

        self.quickSort(arr,start, left-1)
        self.quickSort(arr,left+1,end)

        return arr
