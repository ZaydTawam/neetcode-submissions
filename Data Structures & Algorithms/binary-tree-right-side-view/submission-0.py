# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        right_side_view = []
        curr_lvl = [root]
        while curr_lvl:
            right_side_view.append(curr_lvl[-1].val)
            children = []
            for node in curr_lvl:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            
            curr_lvl = children
        
        return right_side_view