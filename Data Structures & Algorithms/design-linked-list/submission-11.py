class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = LinkNode(0)
        

    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index+1):
            if not cur:
                return -1
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur = self.head
        node = LinkNode(val)
        temp = cur.next
        cur.next = node
        node.next = temp

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur=cur.next
        cur.next = LinkNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        if (index == 0):
            self.addAtHead(val)
            return
        for i in range(index):
            if not cur:
                return
            cur=cur.next
        if not cur.next:
            self.addAtTail(val)
            return
        temp = cur.next
        node = LinkNode(val)
        cur.next = node
        node.next = temp
#[dummy, 0, 1, 2, 3, 4]

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for i in range(index):
            if not cur.next:
                return
            cur = cur.next
        if (cur.next):
            cur.next = cur.next.next
        
        

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)