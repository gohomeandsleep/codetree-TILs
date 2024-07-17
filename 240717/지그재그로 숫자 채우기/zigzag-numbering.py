n, m = map(int,input().split())
lst = [[0 for _ in range(m)] for _ in range(n)]

val = 0
for col in range(m):
    if col % 2 == 0:
        for i in range(n):
            lst[i][col] = val
            val += 1
    else:
        for row in range(n-1, -1, -1):
            lst[row][col] = val
            val += 1 

for row in lst:
    print(' '.join(map(str, row)))