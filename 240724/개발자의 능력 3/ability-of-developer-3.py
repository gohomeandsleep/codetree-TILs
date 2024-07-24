lst = list(map(int, input().split()))

res = float('inf')
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            apart = lst[i] + lst[j] + lst[k]
            bpart = sum(lst) - lst[i] - lst[j] - lst[k]
            res = min(res, abs(apart - bpart))
print(res)