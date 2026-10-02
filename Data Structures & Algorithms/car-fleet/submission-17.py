class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Sort the array based on time to target.
        #Start at the car in the position closest to target
        temp = []
        for i in range(len(position)):
            temp2 = []
            temp2.append(position[i])
            temp2.append(speed[i])
            temp.append(temp2)
        
        temp.sort()
        stack = []
        for car in temp[::-1]:
            stack.append(car)
            #[-1] is newly added car
            #[-2] is car closer to finish line
            if(len(stack)>=2):
                if(stack[-2][0] == stack[-1][0]):
                    stack.pop()
                else:
                    if((target-stack[-2][0])/stack[-2][1] >= (target-stack[-1][0])/stack[-1][1]):
                        stack.pop()
        
        return len(stack)

