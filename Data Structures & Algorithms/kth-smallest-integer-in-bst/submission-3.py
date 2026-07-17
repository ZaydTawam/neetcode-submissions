# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_k(root, count):
            if not root:
                return -1, count
            
            left, new_count = find_k(root.left, count)

            if left == -1:
                new_count += 1
            else:
                return left, new_count

            if new_count == k:
                return root.val, new_count

            return find_k(root.right, new_count)
        
        return find_k(root, 0)[0]