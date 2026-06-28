# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (-1, True)
            
            height_left, balanced_left = dfs(root.left)
            height_right, balanced_right = dfs(root.right)
            balanced = balanced_left and balanced_right and abs(height_left - height_right) <= 1

            return (max(height_left, height_right) + 1, balanced)
        
        return dfs(root)[1]