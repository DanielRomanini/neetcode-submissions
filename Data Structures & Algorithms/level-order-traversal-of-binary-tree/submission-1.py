# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        if not root:
            return arr
        queue = deque()
        queue.append(root)
        while(len(queue)>0):
            temp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)
                if(cur.left):
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
            arr.append(temp)
        return arr

        