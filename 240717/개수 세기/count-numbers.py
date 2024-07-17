n, m = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in lst:
    if i == m:
        res += 1

print(res)