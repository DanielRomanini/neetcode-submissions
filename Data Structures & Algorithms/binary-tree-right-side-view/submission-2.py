# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        queue = deque()
        cur = root
        queue.append(cur)
        while(len(queue)>0):
            temp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur)
                if(cur.left):
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
            arr.append(temp)
        
        final = []
        for i in range(len(arr)):
            final.append(arr[i][-1].val)

        return final
        

                