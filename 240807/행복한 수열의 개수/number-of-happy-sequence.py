n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    tmp_lst = lst[i]
    prev = tmp_lst[0]
    cnt = 1
    stat = True
    for j in range(1, n):
        if tmp_lst[j] == prev:
            cnt += 1
        else:
            if cnt >= k and stat == True:
                res += 1
                stat = False
            prev = tmp_lst[j]
            cnt = 1
    if cnt >= k and stat == True:
        res += 1

for i in range(n):
    tmp_lst = []
    for j in range(n):
        tmp_lst.append(lst[j][i])
    prev = tmp_lst[0]
    cnt = 1
    stat = True
    for j in range(1, n):
        if tmp_lst[j] == prev:
            cnt += 1
        else:
            if cnt >= k and stat == True:
                res += 1
                stat = False
            prev = tmp_lst[j]
            cnt = 1
    if cnt >= k and stat == True:
        res += 1

print(res)