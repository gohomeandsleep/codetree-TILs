n = int(input())

res = 0
for i in range(1, n+1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        res += 1

print(res)