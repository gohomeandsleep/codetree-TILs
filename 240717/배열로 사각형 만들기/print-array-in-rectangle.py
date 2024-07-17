lst = [[1] * 5 for _ in range(5)]

for i in range(1, 5):
    for j in range(1, 5):
        lst[i][j] = lst[i-1][j] + lst[i][j-1]

for row in lst:
    print(' '.join(map(str, row)))