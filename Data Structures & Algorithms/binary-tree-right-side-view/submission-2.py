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

        res = []
        curr_lvl = [root]
        while curr_lvl:
            res.append(curr_lvl[-1].val)
            next_lvl = []
            for node in curr_lvl:
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            curr_lvl = next_lvl
        return res