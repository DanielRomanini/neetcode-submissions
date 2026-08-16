class DoubleLink:
    def __init__(self,prev=None,next=None,val=""):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.tail = DoubleLink(None,None,"tail")
        self.head = DoubleLink(None,self.tail,homepage)
        self.tail.prev = self.head
        self.current = self.head
#[homepage, new, tail]
    def visit(self, url: str) -> None:
        cur = self.current
        node = DoubleLink(cur, self.tail,url)
        cur.next = node
        self.current = node
        self.tail.prev = node


    def back(self, steps: int) -> str:
        
        cur = self.current
        if (cur == self.tail):
            steps+=1
        while steps>0 and (cur.prev):
            cur=cur.prev
            steps-=1        
        if (cur.prev is None):
            self.current = self.head
            return self.current.val
        self.current = cur
        return self.current.val

    def forward(self, steps: int) -> str:
        cur = self.current
        while steps>0 and (cur.next!=self.tail):
            cur=cur.next
            steps-=1
        self.current = cur
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
