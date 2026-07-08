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
        
        current_node = TreeNode(preorder[0])

        subtree_split = inorder.index(preorder[0])
        inorder_left, inorder_right = inorder[:subtree_split], inorder[subtree_split + 1:]
        preorder_left, preorder_right = preorder[1:subtree_split + 1], preorder[subtree_split + 1:]

        current_node.left = self.buildTree(preorder_left, inorder_left)
        current_node.right = self.buildTree(preorder_right, inorder_right)

        return current_node



# 1,2,3,4
# 2,1,3,4

# 2,3,4
# 2