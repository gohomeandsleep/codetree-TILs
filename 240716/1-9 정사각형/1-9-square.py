n = int(input())
res = 0
for i in range(n):
    for j in range(1, n+1):
        res += 1
        if res > 9:
            res -= 9
        print(res, end='')
    print('')