class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = None

    def get(self, key: int) -> int:
        res = self.map.get(key, -1)

        if res == -1:
            return res
        
        if self.tail != res:
            res.prev.next, res.next.prev = res.next, res.prev
            self.tail.next = res
            res.prev, res.next = self.tail, None
            self.tail = res
        
        return res.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            node = self.map[key]
            if self.tail != node:
                node.prev.next, node.next.prev = node.next, node.prev
                self.tail.next = node
                node.prev, node.next = self.tail, None
                self.tail = node

        else:
            print(len(self.map), self.capacity)
            if len(self.map) == self.capacity:
                lru = self.head.next
                self.head.next = lru.next
                if lru.next is not None:
                    lru.next.prev = self.head
                del self.map[lru.key]
            node = Node(key, value)
            self.map[key] = node
            if self.tail is None:
                self.head.next = node
                node.prev = self.head
            else:
                self.tail.next = node
                node.prev = self.tail
            self.tail = node
        


# 1->2