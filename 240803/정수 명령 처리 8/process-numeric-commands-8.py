from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push_f(self, item):
        self.dq.appendleft(item)

    def push_b(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if not self.empty():
            return self.dq.popleft()
        return -1  # 큐가 비어있을 때

    def pop_b(self):
        return self.dq.pop()

    
    def front(self):
        return self.dq[0]


    def back(self):
        return self.dq[-1]


# 명령어 입력 및 실행
n = int(input())
queue = Queue()

for _ in range(n):
    inst = input().split()
    if inst[0] == 'push_front':
        queue.push_f(inst[1])
    elif inst[0] == 'push_back':
        queue.push_b(inst[1])
    elif inst[0] == 'pop_front':
        print(queue.pop())
    elif inst[0] == 'pop_back':
        print(queue.pop_b())
    elif inst[0] == 'size':
        print(queue.size())
    elif inst[0] == 'empty':
        print(1 if queue.empty() else 0)
    elif inst[0] == 'front':
        print(queue.front())
    elif inst[0] == 'back':
        print(queue.back())