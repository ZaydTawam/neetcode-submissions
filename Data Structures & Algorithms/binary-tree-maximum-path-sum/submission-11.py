# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return (float('-INF'), float('-INF'))
            
            l_max_path_sum, l_max_extendable = dfs(root.left)
            r_max_path_sum, r_max_extendable = dfs(root.right)

            curr_max_path_sum = max(
                root.val,
                l_max_path_sum,
                r_max_path_sum,
                root.val + l_max_extendable + r_max_extendable,
                root.val + l_max_extendable,
                root.val + r_max_extendable
            )

            curr_max_extendable = max(
                root.val,
                root.val + l_max_extendable,
                root.val + r_max_extendable
            )

            return (curr_max_path_sum, curr_max_extendable)
        
        return dfs(root)[0]