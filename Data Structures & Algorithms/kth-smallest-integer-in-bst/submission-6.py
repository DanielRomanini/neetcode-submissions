# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        temp = k
        def dfs(root):
            nonlocal temp
            if root.left:
                left = dfs(root.left)

            if (temp == 1):
                arr.append(root.val)
            temp-=1

            if root.right:
                right = dfs(root.right)
        dfs(root)
        return arr[0]