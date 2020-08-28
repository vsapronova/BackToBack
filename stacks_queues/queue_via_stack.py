class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def add_item(self, item):
        self.in_stack.append(item)

    def poll(self):
        if len(self.in_stack) != 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def queue_size(self):
        return (len(self.in_stack) + len(self.out_stack))

    def is_empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0



q = MyQueue()


for el in range(9):
    q.add_item(el)

print(q.in_stack)

q.poll()
q.poll()
print(q.out_stack)