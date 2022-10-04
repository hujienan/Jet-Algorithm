from collections import defaultdict


class ListNode:
    
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        
class DLinkedList:
    
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0
    
    def pop(self, node=None):
        if not node:
            node = self.left.next
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        return node
    
    def append(self, node):
        node.next, node.prev = self.right, self.right.prev
        self.right.prev.next, self.right.prev = node, node
        self.size += 1
        return
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2Node = {}
        self.freq2Dll = defaultdict(DLinkedList)
        self.minFreq = None
        
    def get(self, key: int) -> int:
        if key in self.key2Node:
            node = self.key2Node[key]
            freq = node.freq
            self.freq2Dll[freq].pop(node)
            if self.minFreq == freq and not self.freq2Dll[freq].size:
                self.minFreq += 1
            node.freq += 1
            self.freq2Dll[node.freq].append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key2Node:
            node = self.key2Node[key]
            freq = node.freq
            self.freq2Dll[freq].pop(node)
            if self.minFreq == freq and not self.freq2Dll[freq].size:
                self.minFreq += 1
            node.freq += 1
            self.freq2Dll[node.freq].append(node)
            node.val = value
        else:
            if self.cap == len(self.key2Node):
                node = self.freq2Dll[self.minFreq].pop()
                del self.key2Node[node.key]
            node = ListNode(key, value)
            self.key2Node[key] = node
            self.freq2Dll[1].append(node)
            self.minFreq = 1
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)