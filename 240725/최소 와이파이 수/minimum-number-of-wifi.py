n, m = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
i = m
if m >= n // 2:
    res = 1
elif sum(lst) == 0:
    res = 0
else:
    while i < n:
        #print(i)
        if lst[i - m] == 1:
            res += 1
            i += m + 1
        else:
            i += 1
print(res)