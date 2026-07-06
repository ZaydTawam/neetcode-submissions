# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_tree(root, upper, lower):
            if root is None:
                return True
            return (lower < root.val < upper) and check_tree(root.left, root.val, lower) and check_tree(root.right, upper, root.val)
        
        return check_tree(root, float('inf'), float('-inf'))