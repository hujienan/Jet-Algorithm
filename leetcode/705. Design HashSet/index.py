class MyHashSet:

    def __init__(self):
        self.c = []

    def add(self, key: int) -> None:
        if key not in self.c:
            self.c.append(key)

    def remove(self, key: int) -> None:
        if key in self.c:
            self.c.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.c:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)