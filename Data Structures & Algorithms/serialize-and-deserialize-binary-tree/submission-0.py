# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        tree = [str(root.val)]
        current_level = [root]

        while current_level:
            children = []
            for node in current_level:
                if node.left:
                    tree.append(str(node.left.val))
                    children.append(node.left)
                else:
                    tree.append('x')
                
                if node.right:
                    tree.append(str(node.right.val))
                    children.append(node.right)
                else:
                    tree.append('x')
            current_level = children
        
        return ','.join(tree)
        
    
    # 1, 2, 3, x, x, 
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        tree = data.split(',')
        root = TreeNode(int(tree[0]))
        current_level = [root]
        i = 1
        while current_level:
            next_level = []
            for node in current_level:
                left = right = None
                if tree[i] != 'x':
                    left = TreeNode(int(tree[i]))
                    next_level.append(left)
                if tree[i+1] != 'x':
                    right = TreeNode(int(tree[i+1]))
                    next_level.append(right)
                node.left = left
                node.right = right
                i += 2
            current_level = next_level
        
        return root
