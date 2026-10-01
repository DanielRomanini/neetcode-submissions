class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = []
        for i in range(len(position)):
            temp2 = [position[i],speed[i]]
            temp.append(temp2)
        
        temp.sort(reverse = True, key=lambda num: num[0])
        stack = []
       # print(temp)
        for pos, spd in temp:
            stack.append((target-pos)/spd)
            if(len(stack)>=2):
                if(stack[-2]>=stack[-1]):
                    stack.pop()
        return len(stack)