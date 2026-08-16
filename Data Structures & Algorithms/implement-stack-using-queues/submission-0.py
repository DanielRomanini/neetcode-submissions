class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        arr = self.arr
        arr.append(x)

    def pop(self) -> int:
        arr = self.arr
        return arr.pop()

    def top(self) -> int:
        arr = self.arr
        return arr[len(arr)-1]

    def empty(self) -> bool:
        arr = self.arr
        return len(arr) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()