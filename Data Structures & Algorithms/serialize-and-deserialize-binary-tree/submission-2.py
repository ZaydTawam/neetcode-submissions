from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None: 
            return ""
        output = f"{root.val} "
        curr_lvl = [root]

        while curr_lvl:
            next_lvl = []
            for node in curr_lvl:
                if node.left:
                    output += f"{str(node.left.val)} "
                    next_lvl.append(node.left)
                else:
                    output += "* "
                
                if node.right:
                    output += f"{str(node.right.val)} "
                    next_lvl.append(node.right)
                else:
                    output += "* "
            curr_lvl = next_lvl

        return output

    "1 2 3 * * 4 5"         
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
     
        remaining_values = deque(data.split())
        root = TreeNode(int(remaining_values.popleft()))
        q = deque([root])

        while remaining_values:
            curr = q.popleft()
            left_val = remaining_values.popleft()
            if left_val != '*':
                left = TreeNode(int(left_val))
                curr.left = left
                q.append(left)
                
            right_val = remaining_values.popleft()
            if right_val != '*':
                right = TreeNode(int(right_val))
                curr.right = right
                q.append(right)
        
        return root
