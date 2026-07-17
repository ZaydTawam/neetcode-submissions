# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_tree(root, left_bound, right_bound):
            if not root:
                return True
            return left_bound < root.val < right_bound and check_tree(root.left, left_bound, root.val) and check_tree(root.right, root.val, right_bound)
        
        return check_tree(root, float('-inf'), float('inf'))