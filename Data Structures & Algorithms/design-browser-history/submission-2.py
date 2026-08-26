class LinkNode:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = LinkNode(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        self.current.next = LinkNode(url,None,self.current)
        self.current = self.current.next


    def back(self, steps: int) -> str:
        cur = self.current
        while(cur.prev and steps>0):
            cur = cur.prev
            steps-=1
        self.current = cur
        return cur.val

    def forward(self, steps: int) -> str:
        cur = self.current
        while(cur.next and steps>0):
            cur = cur.next
            steps-=1
        self.current = cur
        return cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)