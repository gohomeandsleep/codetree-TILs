n = int(input())
lst = list(map(int, input().split()))

mxm = 0
for i in range(1, 101):
    cnt = 0
    for j in range(n):
        tmp = 2 * i - lst[j]
        if tmp in lst:
            cnt += 1
    mxm = max(mxm, cnt // 2)
print(mxm)