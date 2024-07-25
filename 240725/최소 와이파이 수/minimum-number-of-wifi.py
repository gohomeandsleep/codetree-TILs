n, m = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
i = m
if sum(lst) == 0:
    res = 0
elif m >= n // 2:
    res = 1
else:
    while i < n:
        #print(i)
        if lst[i - m] == 1:
            res += 1
            i += m + 1
        else:
            i += 1
print(res)