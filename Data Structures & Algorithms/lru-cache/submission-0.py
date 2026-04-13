class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # dummy head and tail so we never deal with empty list edge cases
        self.left = ListNode(0)   # LRU end
        self.right = ListNode(0)  # MRU end
        self.left.next = self.right
        self.right.prev = self.left

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(value, key)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next       # least recently used
            self.remove(lru)
            del self.cache[lru.key]    # need key stored in node for this

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node): # always insert at MRU end (right)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

class ListNode():

    def __init__(self, val=0, key=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
