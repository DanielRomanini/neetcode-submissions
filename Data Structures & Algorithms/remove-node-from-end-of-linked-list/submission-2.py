# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head.next):
            return head.next
        counter = 0
        walker = head
        while(walker):
            counter+=1
            walker = walker.next
        if n>counter:
            return head
        if n == counter:
            return head.next
        element = counter-n
        walker = head
        while(walker.next and element-1>0):
            walker = walker.next
            element-=1
        walker.next = walker.next.next
        return head