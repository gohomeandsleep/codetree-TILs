lst = list(map(int, input().split()))
res = [0 for _ in range(6)]

for i in lst:
    res[i-1] += 1

for i in range(1, 7):
    print("%d - %d" % (i, res[i-1]))