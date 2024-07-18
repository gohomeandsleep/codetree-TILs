class info:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
    
    def __str__(self):
        return f"{self.name} {self.h} {self.w}"

lst = []
for _ in range(5):
    n, h, w = input().split()
    lst.append(info(n, h, w))

lst.sort(key = lambda x:x.name)
print('name')
for i in range(5):
    print(lst[i])
print('')

lst.sort(key = lambda x:x.h)
lst = lst[::-1]
print('height')
for i in range(5):
    print(lst[i])