# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_diameter(root):
            if root is None:
                return (0, -1)
            
            left_max_diameter, left_max_height = get_diameter(root.left)
            right_max_diameter, right_max_height = get_diameter(root.right)

            max_diameter = max(
                left_max_diameter,
                right_max_diameter,
                (left_max_height + right_max_height + 2)
            )
            max_height = max(left_max_height, right_max_height) + 1
            
            return (max_diameter, max_height)
        
        return get_diameter(root)[0]