n = int(input())

res = 0
for i in range(1, n+1):
    for j in range(i):
        res += 1
        print(res, end=' ')
    print(' ')