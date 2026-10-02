class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((i,temp))
                continue
            
            while(len(stack)>0):
                lastIndex = len(stack)-1
                if temp>stack[lastIndex][1]:
                    res[stack[lastIndex][0]] = i - stack[lastIndex][0]
                    stack.pop()
                else:
                    break
            stack.append((i,temp))
            
        
        return res
