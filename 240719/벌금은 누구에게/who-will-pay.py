std, T, k = map(int, input().split())
lst = [0 for _ in range(std)]
res = -1
for i in range(T):
    n = int(input())
    lst[n-1] += 1
    if lst[n-1] == k:
        res = n
        break
    
print(res)