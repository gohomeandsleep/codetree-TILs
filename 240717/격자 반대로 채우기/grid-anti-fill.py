n = int(input())
lst = [[0] * n for _ in range(n)]

val = 1
if n % 2 == 0:
    for i in range(n-1, -1, -1):
        if i % 2 != 0:
            for j in range(n-1, -1, -1):
                lst[j][i] = val
                val += 1
        else:
            for j in range(n):
                lst[j][i] = val
                val += 1
else:
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            for j in range(n-1, -1, -1):
                lst[j][i] = val
                val += 1
        else:
            for j in range(n):
                lst[j][i] = val
                val += 1

for row in lst:
    print(' '.join(map(str, row)))