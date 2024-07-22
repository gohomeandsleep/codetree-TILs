n, k = map(int, input().split())
lst = []
max_l = 0
for _ in range(n):
    p, loc = input().split()
    if int(loc) > max_l:
        max_l = int(loc)
    lst.append([int(loc), int(p)])

point = [0 for _ in range(max_l + 1)]
for i in range(n):
    if point[lst[i][0]] == 0:
        point[lst[i][0]] = lst[i][1]
    else:
        point[lst[i][0]] += lst[i][1]

if 2 * k + 1 > max_l:
    res = sum(point)
else:
    res = 0
    for i in range(max_l - 2 * k + 1):
        #print(i, i + 2 * k + 1, sum(point[i:i + (2 * k) + 1]))
        if sum(point[i:i + (2 * k) + 1]) > res:
            res = sum(point[i:i+(2 * k)+1])
        
print(res)