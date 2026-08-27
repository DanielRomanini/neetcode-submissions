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
        final = []
        queue = deque()
        queue.append(root)
        def bfs(root):
            while(len(queue)>0):
                temp = []
                for i in range(len(queue)):
                    cur = queue.popleft()
                    temp.append(cur.val)
                    if(cur.left):
                        queue.append(cur.left)
                    if(cur.right):
                        queue.append(cur.right)
                final.append(temp)
            return final
        
        last = []
        bfs(root)
        for i in range(len(final)):
            last.append(final[i][-1])
        return last
                    

