n, k = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
if lst[0] > k:
    tmp = 1
else:
    tmp = 0

for i in range(1, n):
    if lst[i] > k:
        tmp += 1
    else:
        if res <= tmp:
            res = tmp
        tmp = 0
    #print(res, tmp)

if res <= tmp:
    res = tmp

if len(lst) == 1:
    if lst[0] > k:
        print(1)
    else:
        print(0)
else:
    print(res)