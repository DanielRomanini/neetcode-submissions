class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.index = k

    def findK(self,val):
        self.arr.sort()
        return self.arr[len(self.arr)-self.index]
#[1,2,3,4,5]


    def add(self, val: int) -> int:
        self.arr.append(val)
        return self.findK(val)
