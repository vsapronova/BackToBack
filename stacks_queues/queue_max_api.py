

class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_cache = []

    def enqueue(self, x):
        self.queue.append(x)
        while len(self.max_cache) != 0 and self.max_cache[-1] < x:
            self.max_cache.pop()
        self.max_cache.append(x)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        value = self.queue.pop(0)
        if value == self.max_cache[0]:
            self.max_cache.pop(0)
        return value

    def max_value(self):
        if len(self.max_cache) == 0:
            return "Queue is empty"
        return self.max_cache[0]

a = MaxQueue()
a.enqueue(100)
a.enqueue(11)
a.enqueue(12)
a.enqueue(6)
a.dequeue()
# a.dequeue()
# a.dequeue()
print(a.max_value())