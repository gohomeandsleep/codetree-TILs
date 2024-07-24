n = int(input())
lst = list(input())

res = 0
for i in range(n):
    if lst[i] == '1':
        continue
    lst[i] = '1'
    p = float('inf')
    if lst[0] == '1':
        cnt = 0
    else:
        cnt = 1
    for j in range(1, n):
        if lst[j] == '1':
            #print(p, res)
            p = min(p, cnt + 1)
            cnt = 0
        else:
            cnt += 1
    res = max(res, p)
    lst[i] = '0'
print(res)