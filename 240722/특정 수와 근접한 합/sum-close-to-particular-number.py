n, k = map(int, input().split())
lst = list(map(int, input().split()))

s = sum(lst)
ans = float("-inf")
for i in range(n):
    for j in range(i+1, n):
        tmp = sum(lst) - lst[i] - lst[j]
        if abs(tmp - k) < abs(ans - k):
            ans = tmp

print(abs(ans - k))