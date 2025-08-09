class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.freq = count
        self.prev = None
        self.next = None
from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = dict()
        self.min_freq = 100006

        # self.most = Node(-1,0,200001)
        # self.least = Node(-2,0,0)
        # self.most.next = self.least
        # self.least.prev = self.most

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.freq[node.freq].pop(key)
            if node.freq == self.min_freq and len(self.freq[node.freq]) == 0:
                self.min_freq = node.freq+1
            node.freq += 1
            if self.freq.get(node.freq, -1) == -1:
                self.freq[node.freq] = OrderedDict()
            self.freq[node.freq][key] = node
            # print(self.cache.keys())
            return node.val
        # print(self.cache.keys())
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # print(self.cache[key])
            node = self.cache[key]
            self.freq[node.freq].pop(key)
            if node.freq == self.min_freq and len(self.freq[node.freq]) == 0:
                self.min_freq = node.freq+1

            node.freq += 1
            node.val = value

            if self.freq.get(node.freq, -1) == -1:
                self.freq[node.freq] = OrderedDict()

            self.cache[key] = node
            self.freq[node.freq][key] = node
            # print(self.cache)
        else:
            node = Node(key, value, 1)
            if self.freq.get(1, -1) == -1:
                self.freq[1] = OrderedDict()
            if len(self.cache) == self.capacity:
                temp = self.freq[self.min_freq].popitem(last=False)
                # print(temp[1])
                self.cache.pop(temp[0])
                self.min_freq = 1
                self.cache[key] = node
                self.freq[1][key] = node
            else:
                self.min_freq = 1
                self.cache[key] = node
                self.freq[1][key] = node
            # print(self.cache)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)