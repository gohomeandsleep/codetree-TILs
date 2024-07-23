n= int(input())
lst = []
max_l = 0
for _ in range(n):
    loc, p = input().split()
    if int(loc) > max_l:
        max_l = int(loc)
    lst.append([int(loc), p])
lst.sort(key = lambda x:x[0])

point = [' ' for _ in range(max_l + 1)]
for i in range(n):
    point[lst[i][0]] = lst[i][1]

mxm = 0
for i in range(1, max_l):
    for j in range(i+1, max_l):
        #print(i, j, point[i], point[j])
        if point[i] != ' ' and point[j] != ' ':
            cnt_g = point[i:j].count('G')
            cnt_h = point[i:j].count('H')
            #print(cnt_g, cnt_h)
            if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
                mxm = max(mxm, len(point[i:j]) + 1)
print(mxm)