class LinkNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = LinkNode()           
        self.size = 0

    def get(self, index: int) -> int:
        if (index>=self.size):
            return -1
        cur = self.head
        while(index>=0):
            cur = cur.next
            index-=1
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head
        temp = cur.next
        cur.next = LinkNode(val,temp)
        self.size+=1


    def addAtTail(self, val: int) -> None:
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = LinkNode(val)
        self.size+=1
#[1,2,3,4,5]        index 2(after 2, before 3)
    def addAtIndex(self, index: int, val: int) -> None:
        if (index == self.size):
            self.addAtTail(val)
        elif (index == 0):
            self.addAtHead(val)
        else:
            cur =self.head
            while(index>0):
                cur = cur.next
                index-=1
            temp = cur.next
            cur.next = LinkNode(val,temp)
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if (index>=self.size):
            return
        cur = self.head
        while(index>0):
            cur = cur.next
            index-=1
        cur.next = cur.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)