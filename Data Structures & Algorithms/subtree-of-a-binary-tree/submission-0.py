# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    return root1.val == root2.val and is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        is_subtree = False
        if root.val == subRoot.val:
            is_subtree = is_same_tree(root, subRoot)
        
        return is_subtree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)