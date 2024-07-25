n = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = []
for i in range(n):
    res.append(lst[i])
for i in range(n):
    res[i] = abs(res[i] - lst[n+i])

print(min(res))