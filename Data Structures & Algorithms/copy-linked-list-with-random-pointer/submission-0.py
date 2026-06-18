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
        indexes = {}
        arr = []
        curr = head
        i = 0
        dummy = prev = Node(0)
        new_list = None
        while curr:
            indexes[curr] = i
            new_list = Node(curr.val)
            arr.append(new_list)
            prev.next = new_list
            prev = prev.next
            new_list = new_list.next
            curr = curr.next
            i += 1

        new_head = dummy.next

        curr_old = head
        curr_new = new_head
        while curr_old:
            if curr_old.random:
                random_node = arr[indexes[curr_old.random]]
                curr_new.random = random_node
            curr_old, curr_new = curr_old.next, curr_new.next
        
        return new_head

