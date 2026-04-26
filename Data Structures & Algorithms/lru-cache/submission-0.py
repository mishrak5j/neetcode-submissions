class DoubleLinkedList:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = DoubleLinkedList(0,0), DoubleLinkedList(0,0)
        self.left.next, self.right.prev  = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        nxt.prev = node
        node.prev, node.next = prv, nxt

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DoubleLinkedList(key, value)
        self.insert(self.cache[key])

        if len(self.cache)> self.cap:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]


        
