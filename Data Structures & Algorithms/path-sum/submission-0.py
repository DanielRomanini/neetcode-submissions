# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,arr,targetSum):
        if not root:
            return False
        arr.append(root.val)
        
        if not root.left and not root.right:
            sum = 0
            for i in range(len(arr)):
                sum += arr[i]
            if sum == targetSum:
                return True
            else:
                arr.pop()
                return False

        if (self.dfs(root.left,arr,targetSum)):
            return True
        if (self.dfs(root.right,arr,targetSum)):
            return True
        arr.pop()
        return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr = []
        return self.dfs(root,arr,targetSum)