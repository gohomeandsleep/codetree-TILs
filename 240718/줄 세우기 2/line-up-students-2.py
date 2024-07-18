class std:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

    def __str__(self):
        return f"{self.height} {self.weight} {self.idx}"

n = int(input())
lst = []
for i in range(1, n+1):
    h, w = map(int ,input().split())
    lst.append(std(h, w, i))

lst.sort(key = lambda x:(x.height, -x.weight))

for i in range(n):
    print(lst[i])