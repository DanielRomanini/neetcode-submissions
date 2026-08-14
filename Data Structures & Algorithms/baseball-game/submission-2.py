class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []
        for i in operations:
            if (i == "D"):
                stack.append(stack[-1]*2)
            elif (i=="C"):
                stack.pop()
            elif (i=="+"):
                temp = (stack[-1]) + (stack[-2])
                stack.append(temp)
            else:
                stack.append(int(i))
        for i in range(len(stack)):
            score+=int(stack[i])
        return score