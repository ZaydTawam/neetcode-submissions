# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes_count = 0
        def dfs(max_val, root):
            nonlocal good_nodes_count
            if root is None:
                return
            if root.val >= max_val:
                good_nodes_count += 1
                max_val = root.val
            dfs(max_val, root.left)
            dfs(max_val, root.right)
        
        dfs(float('-INF'), root)
        return good_nodes_count
