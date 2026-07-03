# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head
        while True:
            min_node = None
            for i, node in enumerate(lists):
                if not node:
                    continue
                if not min_node or min_node[1].val > node.val:
                    min_node = (i, node)

            if min_node == None:
                break
            
            lists[min_node[0]] = min_node[1].next

            curr.next = min_node[1]
            curr = curr.next
        
        return dummy_head.next
            
                
            
# 0,1,1,2,3,3,4,5,6
# 
# ^
# 
# ^
# 
# ^


# 
# ^
# 1,1,2,3,3,4,5
#           ^ ^
# ,6
# ^