n, m = map(int, input().split())

res = 0
for i in range(n, m+1):
    res += i

print(res)