n, k = map(int, input().split())
lst = []
max_l = 0
for _ in range(n):
    loc, p = input().split()
    if int(loc) > max_l:
        max_l = int(loc)
    if p == 'G':
        lst.append([int(loc), 1])
    elif p == 'H':
        lst.append([int(loc), 2])

point = [0 for _ in range(max_l + 1)]
for i in range(n):
    point[lst[i][0]] = lst[i][1]

res = 0
for i in range(max_l - k):
    if sum(point[i:i+k+1]) > res:
        res = sum(point[i:i+k+1])

print(res)