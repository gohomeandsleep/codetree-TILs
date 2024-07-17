n = int(input())
lst = list(map(int, input().split()))

res = float('inf')
for i in range(len(lst)-1):
    if lst[i+1]- lst[i] < res:
        res = lst[i+1] - lst[i]

print(res)