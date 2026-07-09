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
                return (float('-inf'), 0)
            
            max_path_sum_left, best_extendable_path_left = dfs(root.left)
            max_path_sum_right, best_extendable_path_right = dfs(root.right)

            max_path_sum = max(
                root.val,
                root.val + best_extendable_path_left,
                root.val + best_extendable_path_right,
                root.val + best_extendable_path_left + best_extendable_path_right,
                max_path_sum_left,
                max_path_sum_right,
            )
            best_extendable_path = max(
                root.val,
                root.val + best_extendable_path_left,
                root.val + best_extendable_path_right,
            )

            return (max_path_sum, best_extendable_path)
        
        return dfs(root)[0]
            

