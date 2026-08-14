class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = 0
        closed = 0
        if (len(s) <= 1 or s[0] in [")","}","]"]):
            return False
        for bracket in s:
            if (bracket in ["(","[","{"]):
                stack.append(bracket)
                opened+=1
            elif (len(stack) != 0 and bracket == ")" and stack[-1] == "("):
                stack.pop()
                closed+=1
            elif (len(stack) != 0 and bracket == "]" and stack[-1] == "["):
                stack.pop()
                closed+=1
            elif (len(stack) != 0 and bracket == "}" and stack[-1] == "{"):
                stack.pop()
                closed+=1
            else:
                return False
        if (opened != closed):
            return False
        return True
            
