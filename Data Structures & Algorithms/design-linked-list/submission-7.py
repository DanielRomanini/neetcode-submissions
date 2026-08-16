class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0) #Creates a dummy node
        self.size = 0

    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index+1):
            if not cur:
                return -1
            cur=cur.next
        if cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        temp = ListNode(val)               #[dummy,1,2,3,3]
        temp2 = self.head.next
        self.head.next = temp
        temp.next = temp2
    


    def addAtTail(self, val: int) -> None:
        temp = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = temp

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        if (index == 0):
            self.addAtHead(val)
            return
        for i in range(index):
            if not cur:
                return 
            cur=cur.next
        temp = cur.next
        cur.next = ListNode(val)
        cur.next.next = temp
        
            

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for i in range(index):
            if not cur.next:
                return
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
            
        
        
#[dummy, 1, 2, 3, 4, 5]
#[  0,   1, 2, 3, 4, 5]

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)