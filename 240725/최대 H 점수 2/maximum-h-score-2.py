n, l = map(int, input().split())
lst = list(map(int, input().split()))

mxm = 0
for i in range(1, 101):
    cnt = 0
    for j in range(n):
        if lst[j] >= i:
            cnt += 1
    if cnt >= i:
        mxm = i
    else:
        less = i - cnt
        if less <= lst.count(i-1) and less <= l:
            mxm = i
print(mxm)