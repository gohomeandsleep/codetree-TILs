n = int(input())

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print("(%d,%d)" % (i, j), end=' ')
    print('')