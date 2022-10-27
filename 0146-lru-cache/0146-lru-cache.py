# Approach 2: Hashmap + DoubleLinkedList

# get & put the key: standard hashmap
# delete the first added key: linked list

# T.C. = O(1) all operations are done in a constant time
# S.C. = O(capacity) ordered dictionary with at most capacity + 1 elements

# NODE inse double linked list
class Node():
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # helper1 remove existing node
    def remove(self, node: [Node]):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    # helper2 insert a node at the end (before tail)
    def insert(self, node: [Node]):
        prevNode = self.tail.prev
        nextNode = self.tail
        prevNode.next = node
        nextNode.prev = node
        node.next = nextNode
        node.prev = prevNode
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)