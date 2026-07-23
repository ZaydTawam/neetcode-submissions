# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        tree_split = inorder.index(preorder[0])
        left_preorder, left_inorder = preorder[1:tree_split + 1], inorder[:tree_split]
        right_preorder, right_inorder = preorder[tree_split + 1:], inorder[tree_split + 1:]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root