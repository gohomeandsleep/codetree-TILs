n = int(input())

res = 0
for i in range(1, n+1):
    if i % 400 == 0:
        res += 1
    elif i % 100 == 0:
        res += 0
    elif i % 4 == 0:
        res += 1

print(res)