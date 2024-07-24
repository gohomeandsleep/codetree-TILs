lst = list(map(int, input().split()))

res = float('inf')
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            for l in range(k+1, len(lst)):
                if i == j or j == k or k == l or i == k or j == l or i == l:
                    continue
                sum1 = lst[i] + lst[j]
                sum2 = lst[k] + lst[l]
                sum3 = sum(lst) - lst[i] - lst[j] - lst[k] - lst[l]
                #print(sum1, sum2, sum3)
                tmp = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
                res = min(res, tmp)
print(res)