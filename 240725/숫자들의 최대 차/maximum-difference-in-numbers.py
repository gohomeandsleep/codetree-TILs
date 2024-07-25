n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

mxm = 0
for i in range(n):
    for j in range(i+1, n):
        if lst[j] - lst[i] <= k:
            mxm = max(mxm, len(lst[i:j]))
print(mxm + 1)