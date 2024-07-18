class point:
    def __init__(self, dist, idx):
        self.dist = dist
        self.idx = idx

    def __str__(self):
        return f"{self.idx}"

n = int(input())
lst = []
for i in range(1, n+1):
    x, y = map(int, input().split())
    lst.append(point(abs(x)+abs(y), i))

lst.sort(key = lambda x:x.dist)

for i in range(n):
    print(lst[i])