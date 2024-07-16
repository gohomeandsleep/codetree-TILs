n = int(input())

res = 0
for i in range(n):
    for j in range(i):
        print("  ", end='')
    for j in range(n-i):
        res += 1
        if res > 9:
            res -= 9
        print(res, end=' ')
    print('')