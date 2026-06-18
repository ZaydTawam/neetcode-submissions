"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_index = {}
        copied_nodes = []
        
        dummy = Node(0)
        prev = dummy
        curr = head
        i = 0
        while curr:
            node_index[curr] = i
            new_node = Node(curr.val)
            copied_nodes.append(new_node)
            prev.next = new_node
            prev = new_node
            curr = curr.next
            i += 1

        new_head = dummy.next

        curr_old = head
        curr_new = new_head
        while curr_old:
            if curr_old.random:
                curr_new.random = copied_nodes[node_index[curr_old.random]]
            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return new_head

