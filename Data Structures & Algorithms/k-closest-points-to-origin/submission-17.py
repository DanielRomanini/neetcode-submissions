class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p = []
        dist = []
        
        for i in range(len(points)):
            dist.append((points[i][0])**2+(points[i][1])**2)
            points[i].append((points[i][0])**2+(points[i][1])**2)
        
        heapq.heapify(dist)
        while(k>0):
            p.append(heapq.heappop(dist))
            k-=1
        final = []
        for i in range(len(points)):
            if points[i][2] in p:
                temp = []
                temp.append(points[i][0])
                temp.append(points[i][1])
                final.append(temp)
        return final


        