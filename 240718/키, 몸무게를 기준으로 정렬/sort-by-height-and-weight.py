class info:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
    
    def __str__(self):
        return f"{self.name} {self.h} {self.w}"

n = int(input())
lst = []
for _ in range(n):
    name, h, w = input().split()
    lst.append(info(name, int(h), int(w)))

lst.sort(key = lambda x:(x.h, -x.w))

for i in range(n):
    print(lst[i])