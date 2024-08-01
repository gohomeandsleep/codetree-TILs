from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def pop(self):
        return self.dq.popleft()

    def pop_push(self):
        tmp = self.dq.popleft()
        self.dq.append(tmp)

    def size(self):
        return len(self.dq)

n = int(input())
queue = Queue()

for i in range(1, n+1):
    queue.push(i)

while queue.size() != 1:
    queue.pop()
    queue.pop_push()

print(queue.pop())