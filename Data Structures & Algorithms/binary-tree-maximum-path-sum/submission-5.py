# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            
            if not root.left and not root.right:
                return (root.val, root.val)
            
            max_path_sum_left, connected_left = dfs(root.left)
            max_path_sum_right, connected_right = dfs(root.right)

            max_path_sum = max(
                root.val,
                root.val + connected_left,
                root.val + connected_right,
                root.val + connected_left + connected_right,
                max_path_sum_left or float('-inf'),
                max_path_sum_right or float('-inf'),
            )
            connected = max(
                root.val,
                root.val + connected_left,
                root.val + connected_right,
            )

            return (max_path_sum, connected)
        
        return dfs(root)[0]
            

