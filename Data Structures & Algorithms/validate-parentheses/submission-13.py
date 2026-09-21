class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            print(char)
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                popped = stack.pop()
                print(popped)
                if char == '}' and popped != '{':
                    return False
                if char == ']' and popped != '[':
                    return False
                if char == ')' and popped != '(':
                    return False
        if(len(stack) == 0):
            return True
        return False