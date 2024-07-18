n = int(input())

lst = [[' '] * n for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        lst[0][i] = '*'
    else:
        for j in range(i+1):
            lst[j][i] = '*'

for row in lst:
    print(*row, sep=' ')