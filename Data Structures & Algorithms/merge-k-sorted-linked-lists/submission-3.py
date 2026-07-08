# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list_head = curr = ListNode()
        while True:
            min_node = None
            min_node_index = 0
            for i, node in enumerate(lists):
                if node and (min_node is None or node.val < min_node.val):
                    min_node = node
                    min_node_index = i
            if min_node is None:
                break
            curr.next = min_node
            curr = curr.next
            lists[min_node_index] = min_node.next
        
        return new_list_head.next
            