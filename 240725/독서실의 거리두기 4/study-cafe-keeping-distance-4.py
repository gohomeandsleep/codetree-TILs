n = int(input())
lst = list(input())

res = 0
for i in range(n): #i, j = 자리
    for j in range(i+1, n):
        if lst[i] == '1' or lst[j] == '1' or i == j:
            continue
        lst[i] = lst[j] = '1'
        p = float('inf')
        k = 0           #k = 이동하는 자리수
        while lst[k] == '0':
            k += 1
        cnt = 0
        for l in range(k+1, n):
            if lst[l] == '1':
                p = min(p, cnt + 1)
                cnt = 0
            else:
                cnt += 1
        res = max(res, p)
        lst[i] = lst[j] = '0'
print(res)