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
        
        node_indicies = {}
        copied_nodes = []
        dummy = new_curr = Node(0)
        old_curr = head
        i = 0
        while old_curr:
            node_indicies[old_curr] = i
            new_curr.next = Node(old_curr.val)
            new_curr = new_curr.next
            copied_nodes.append(new_curr)
            old_curr = old_curr.next
            i += 1
            
        curr_old = head
        curr_new = dummy.next
        while curr_old:
            if curr_old.random:
                index_of_random = node_indicies.get(curr_old.random)
                curr_new.random = copied_nodes[index_of_random]
            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return dummy.next
        