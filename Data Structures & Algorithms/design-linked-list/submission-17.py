class LinkNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = LinkNode(0)
        self.size = 0
#[dummy,1,3,]

    def get(self, index: int) -> int:
        cur = self.dummy
        for i in range(index+1):
            if not cur:
                return -1
            cur = cur.next
        if not cur:
            return-1
        return cur.val


    def addAtHead(self, val: int) -> None:
        cur = self.dummy
        temp = cur.next
        cur.next = LinkNode(val)
        cur = cur.next 
        cur.next = temp
        self.size+=1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        while(cur.next):
            cur = cur.next
        cur.next = LinkNode(val)
        self.size+=1
#[dummy,0,1,2,3]

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.dummy
        if (index == 0):
            self.addAtHead(val)
            return
        for i in range(index):
            if not cur:
                return
            cur = cur.next
        temp = cur.next
        cur.next = LinkNode(val)
        cur = cur.next
        cur.next = temp
        
        #[dummy,2,1,2,0,6,]

        

    def deleteAtIndex(self, index: int) -> None:
        cur=self.dummy
        while(cur and index>0 and cur.next):
            cur = cur.next
            index-=1
        if cur.next:
            cur.next = cur.next.next
        self.size-=1
#[dummy,2,1,2,0,6,]

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)