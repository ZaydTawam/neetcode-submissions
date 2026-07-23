# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {n: i for i, n in enumerate(inorder)}

        def helper(preorder_start, inorder_start, subtree_size):
            if not subtree_size:
                return None
            root = TreeNode(preorder[preorder_start])
            tree_split = inorder_map[preorder[preorder_start]]
            left_subtree_size, right_subtree_size = tree_split - inorder_start, subtree_size - tree_split + inorder_start - 1
            root.left = helper(preorder_start + 1, inorder_start, left_subtree_size)
            root.right = helper(preorder_start + left_subtree_size + 1, tree_split + 1, right_subtree_size)
            
            return root

        return helper(0, 0, len(preorder))