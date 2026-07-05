# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        curr_lvl = [root]
        while curr_lvl:
            curr_lvl_vals = []
            children = []
            for node in curr_lvl:
                curr_lvl_vals.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(curr_lvl_vals)
            curr_lvl = children
        
        return res