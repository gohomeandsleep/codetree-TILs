n = int(input())
lst = [int(input()) for _ in range(n)]

res = 0
tmp = 1
for i in range(1, n):
    if lst[i-1] == lst[i]:
        tmp += 1
    else:
        if res <= tmp:
            res = tmp
        tmp = 1
    #print(tmp, res)

if len(lst) == 1:
    print(1)
else:
    print(res)