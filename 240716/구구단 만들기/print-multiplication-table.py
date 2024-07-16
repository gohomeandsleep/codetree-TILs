n, m = map(int ,input().split())

for i in range(1, 10):
    for j in range(m, n-1, -2):
        if j % 2 == 0:
            print("%d * %d = %d" % (j, i, i*j), end='')
            if j != n:
                print(' /', end=' ')
    print('')