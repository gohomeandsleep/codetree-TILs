n, k = map(int, input().split())

lst = [0 for _ in range(n)]
for i in range(k):
    stp, endp = map(int, input().split())
    for j in range(endp - stp + 1):
        lst[stp + j -1] += 1

print(max(lst))