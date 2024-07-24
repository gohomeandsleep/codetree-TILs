n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

mxm = -1
for i in range(n):
    if lst[i] in lst[i+1:i+k+1]:
        mxm = max(mxm, lst[i])
print(mxm)