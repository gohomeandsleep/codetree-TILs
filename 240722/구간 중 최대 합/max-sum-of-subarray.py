n, k = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(n - k + 1):
    if sum(lst[i:i+k]) > res:
        res = sum(lst[i:i+k])

print(res)