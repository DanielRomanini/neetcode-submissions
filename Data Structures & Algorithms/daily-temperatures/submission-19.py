class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counter = 0
        res = [0] * len(temperatures)
        stack = []
        for i, tempe in enumerate(temperatures):
            if(len(stack)<1):
                stack.append([tempe,i])
                continue
            
            while(len(stack)>0 and tempe>stack[-1][0]):
                temp = stack.pop()
                res[temp[1]] = i-temp[1]
            stack.append([tempe,i])
                
        
        return res
