lst = list(map(int, input().split()))
res = [0 for _ in range(10)]

for i in range(len(lst)):
    if lst[i] == 0:
        break
    tmp = lst[i] // 10
    if tmp > 0:
        res[tmp-1] += 1

res = res[::-1]
for i in range(10):
    print("%d - %d" % (10 * (10-i), res[i]))