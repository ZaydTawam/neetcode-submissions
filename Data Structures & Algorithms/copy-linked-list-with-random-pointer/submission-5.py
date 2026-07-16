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
        new_list = []

        curr_old = head
        dummy = curr_new = Node(0)
        i = 0
        while curr_old:
            node_indicies[curr_old] = i
            i += 1

            curr_new.next = Node(curr_old.val)
            curr_new = curr_new.next
            new_list.append(curr_new)
            curr_old = curr_old.next
        
        curr_old = head
        curr_new = dummy.next
        while curr_old:
            if curr_old.random:
                index = node_indicies[curr_old.random]
                curr_new.random = new_list[index]
            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return dummy.next