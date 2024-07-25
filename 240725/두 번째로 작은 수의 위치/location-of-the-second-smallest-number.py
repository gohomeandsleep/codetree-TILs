n = int(input())
lst = list(map(int, input().split()))

tmp = lst[:]
smallest = min(tmp)
for i in tmp:
    if i == smallest:
        tmp.remove(i)
second = min(tmp)

if lst.count(second) >= 2:
    print(-1)
else:
    print(lst.index(second) + 1)