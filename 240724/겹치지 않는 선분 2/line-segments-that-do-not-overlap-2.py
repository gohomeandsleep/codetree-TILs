n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    stat = True
    tmp = lst.pop(0)
    for j in range(n - 1):
        x = lst[j][0]
        y = lst[j][1]
        if x > tmp[0]:
            if y < tmp[1]:
                stat = False
        else:
            if y > tmp[1]:
                stat = False
        #print(tmp, x, y, stat)
    if stat == True:
        cnt += 1
    lst.append(tmp)
print(cnt)