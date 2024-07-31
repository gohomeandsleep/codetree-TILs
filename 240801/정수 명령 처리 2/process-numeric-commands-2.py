from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        return self.dq.popleft()
    
    def front(self):
        return self.dq[0]

n = int(input())
queue = Queue()

for _ in range(n):
    inst = list(input().split())
    if inst[0] == 'push':
        queue.push(inst[1])
    elif inst[0] == 'pop':
        print(queue.pop())
    elif inst[0] == 'size':
        print(queue.size())
    elif inst[0] == 'empty':
        if queue.size() == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == 'front':
        print(queue.front())