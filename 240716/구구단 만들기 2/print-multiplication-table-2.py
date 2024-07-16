n, m = map(int, input().split())

for i in range(2, 10, 2):
    for j in range(m, n-1, -1):
        print("%d * %d = %d" % (j, i, i*j), end='')
        if j != n:
            print(' /', end=' ')
    print('')