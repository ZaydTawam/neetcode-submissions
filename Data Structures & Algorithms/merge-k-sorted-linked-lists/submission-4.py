from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i, head in enumerate(lists):
            if head is not None:
                heappush(h, (head.val, i))
        
        dummy = curr = ListNode()
        while h:
            node_index = heappop(h)[1]
            next_node = lists[node_index]
            curr.next = next_node
            if next_node.next is not None:
                heappush(h, (next_node.next.val, node_index))
                lists[node_index] = next_node.next
            
            curr = curr.next
        
        return dummy.next
            
             