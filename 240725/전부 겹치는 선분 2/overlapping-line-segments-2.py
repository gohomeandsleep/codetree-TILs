n = int(input())
lst = [0 for _ in range(101)]
for _ in range(n):
    stp, endp = map(int, input().split())
    for i in range(stp, endp+1):
        lst[i] += 1

res = 'No'
for i in range(101):
    if lst[i] == n - 1:
        res = 'Yes'
print(res)