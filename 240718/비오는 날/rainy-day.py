class date:
    def __init__(self, d, t):
        self.d = d
        self.t = t

    def __str__(self):
        return f"{self.d} {self.t}"

n = int(input())
lst = []
for _ in range(n):
    d, t, w = input().split()
    if w == 'Rain':
        lst.append(date(d, t))

if lst:
    lst.sort(key=lambda x: x.d)
    print(lst[0], end=' ')
    print('Rain')