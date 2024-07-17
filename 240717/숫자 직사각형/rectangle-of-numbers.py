n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(m * i + j + 1, end=' ')
    print('')