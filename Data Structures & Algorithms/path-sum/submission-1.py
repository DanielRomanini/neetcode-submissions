# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        count = []

        def dfs(root):
            if not root:
                return False
            count.append(root.val)

            if not root.left and not root.right:
                if sum(count) == targetSum:
                    return True
                else:
                    count.pop()
                    return False
            
            if(dfs(root.left)):
                return True
            if(dfs(root.right)):
                return True
            count.pop()
            return False
        
        return dfs(root)