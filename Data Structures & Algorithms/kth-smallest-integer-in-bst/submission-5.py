# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,root,arr):
        cur = root
         
        if not cur:
            return 0

        left = self.check(cur.left,arr)
        arr.append(cur)
        right = self.check(cur.right,arr)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.check(root,arr)
        return arr[k-1].val
