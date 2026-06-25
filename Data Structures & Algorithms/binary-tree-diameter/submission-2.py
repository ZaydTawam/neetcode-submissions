# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (-1, 0)
            
            height_left, diameter_left = dfs(root.left)
            height_right, diameter_right = dfs(root.right)

            max_diameter = max(height_left + height_right + 2, max(diameter_left, diameter_right))

            return (max(height_left + 1, height_right + 1), max_diameter)
        
        return dfs(root)[1]