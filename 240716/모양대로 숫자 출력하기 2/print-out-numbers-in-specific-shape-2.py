n = int(input())
res = 0
for i in range(n):
    for j in range(1, n+1):
        res += 2
        if res > 8:
            res -= 8
        print(res, end=' ')
    print('')