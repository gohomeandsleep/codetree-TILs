n = int(input())
lst = list(input())

res = 0
for i in range(n):
    if lst[i] == '1':
        continue
    lst[i] = '1'
    p = float('inf')
    j = 0
    while lst[j] == '0':
        j += 1
    #print(j)
    cnt = 0
    for k in range(j+1, n):
        if lst[k] == '1':
            #print(p, res)
            p = min(p, cnt + 1)
            cnt = 0
        else:
            cnt += 1

    res = max(res, p)
    lst[i] = '0'
print(res)