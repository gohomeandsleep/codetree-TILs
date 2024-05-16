n = int(input())

lst = [0 for _ in range(201)]

for _ in range(n):
    stp, endp = map(int, input().split())
    for j in range(endp - stp):
        lst[100 + stp + j+1] += 1

print(max(lst))