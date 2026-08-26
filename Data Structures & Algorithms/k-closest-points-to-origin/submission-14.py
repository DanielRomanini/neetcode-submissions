class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):
            temp = []
            temp.append(math.sqrt((points[i][0])**2+(points[i][1])**2))
            temp.append(i)
            dist.append(temp)
            print(dist[i][0], dist[i][1])
        print("----------------------")
        dist.sort()
        
        final = []
        for i in range(k):
            final.append(points[dist[i][1]])

        return final
        
        