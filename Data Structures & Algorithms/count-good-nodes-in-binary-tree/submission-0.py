# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root, largest_ancestor):
            if not root:
                return 0
            if root.val >= largest_ancestor:
                return 1 + count(root.left, root.val) + count(root.right, root.val)
            else:
                return count(root.left, largest_ancestor) + count(root.right, largest_ancestor)
        
        return count(root, float('-inf'))