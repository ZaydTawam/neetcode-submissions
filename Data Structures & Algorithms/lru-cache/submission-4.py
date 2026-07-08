class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head        

    def move_front(self, node: ListNode):
        if node.key in self.cache:
            node.prev.next, node.next.prev = node.next, node.prev
        
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node is None:
            return -1
        
        self.move_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.move_front(node)
        
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                lru.prev.next, lru.next.prev = lru.next, lru.prev
                del self.cache[lru.key]
            new_node = ListNode(key, value)
            self.move_front(new_node)
            self.cache[key] = new_node
