n = int(input())

res = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            res += 1
            print(res, end=' ')
    else:
        for j in range(n):
            res += 2
            print(res, end=' ')
    print('')