class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.key2Node = {}
        self.cap = capacity
        self.left = LinkedList(-1, -1)
        self.right = LinkedList(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def insert(self, node):
        mru = self.right.prev
        mru.next, node.prev = node, mru
        self.right.prev, node.next = node, self.right
        
    def get(self, key: int) -> int:
        if key in self.key2Node:
            node = self.key2Node[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key2Node:
            self.remove(self.key2Node[key])
            node = LinkedList(key, value)
            self.insert(node)
            self.key2Node[key] = node
            return
        if len(self.key2Node) == self.cap:
            keyToDelete = self.left.next.key
            del self.key2Node[keyToDelete]
            self.remove(self.left.next)
        node = LinkedList(key, value)
        self.insert(node)
        self.key2Node[key] = node
        return
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)