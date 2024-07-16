n = int(input())
res = 10
for i in range(n):
    for j in range(1, n+1):
        res -= 1
        if res < 1:
            res += 9
        print(res, end='')
    print('')