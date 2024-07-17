n = int(input())
lst = list(map(int, input().split()))
 
if lst == sorted(lst, reverse=True):
    print(0)
else:
    res = float('-inf')
    for i in range(n):
        for j in range(i, n):
            if lst[j] - lst[i] > res:
                res = lst[j] - lst[i]
    print(res)