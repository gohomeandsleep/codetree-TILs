n = int(input())
res = 0
for _ in range(n):
    res += int(input())

res = list(str(res))
res.append(res.pop(0))
print(*res, sep='')