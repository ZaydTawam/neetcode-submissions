# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root, count):
            if root is None:
                return (None, count)

            node, count = inorder(root.left, count)

            if node:
                return (node, count)
            
            count += 1
            
            if count == k:
                return (root.val, count)
            
            return inorder(root.right, count)
        
        return inorder(root, 0)[0]
        