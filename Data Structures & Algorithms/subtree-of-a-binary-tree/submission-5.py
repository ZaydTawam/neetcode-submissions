# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(root_a, root_b):
    if root_a is None and root_b is None:
        return True
    
    if root_a is None or root_b is None:
        return False
    
    if root_a.val != root_b.val:
        return False
    
    return isSameTree(root_a.left, root_b.left) and isSameTree(root_a.right, root_b.right)

class Solution: 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 