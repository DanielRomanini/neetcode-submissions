class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.limit = capacity
        self.queue = deque()


    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.queue.remove(key)
            self.queue.append(key)
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if(key in self.hashmap):
            self.queue.remove(key)
        if (len(self.queue)>=self.limit):
            del self.hashmap[self.queue.popleft()]

        self.queue.append(key)
        self.hashmap[key] = value
        
