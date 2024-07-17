lst = list(map(int, input().split()))
res = [0 for _ in range(9)]

for i in range(len(lst)):
    if lst[i] == 0:
        break
    tmp = lst[i] // 10
    if tmp >= 1:
        res[tmp-1] += 1

for i in range(9):
    print("%d - %d" % (i+1, res[i]))