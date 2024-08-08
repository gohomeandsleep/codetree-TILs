n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
stpy, stpx, rup, lup, ldown, rdown, d = map(int, input().split())

tmp_lst = [[0 for _ in range(rup+1)] for _ in range(lup+1)]
tmpx = stpx-1-rdown
tmpy = stpy-1-rdown
for j in range(lup+1):  # tmp_lst y 좌표
    for k in range(rup+1):  # tmp_lst x 좌표
        tmp_lst[j][k] = lst[tmpy - k][tmpx + k]
    tmpx += 1
    tmpy += 1

w = rup + 1 # tmp_lst 가로
h = lup + 1 # tmp_lst 세로

if d == 0: # Counter-clockwise rotation
    tmp1 = tmp_lst[0][1:]
    tmp3 = tmp_lst[h-1][:-1]
    tmp2 = []
    tmp4 = []
    for i in range(h-1):
        tmp2.append(tmp_lst[i][0])
        tmp4.append(tmp_lst[i+1][w-1])
    for i in range(w-1):
        tmp_lst[0][i] = tmp1[i]
    for i in range(h-1):
        tmp_lst[i+1][0] = tmp2[i]
    for i in range(w-1):
        tmp_lst[h-1][i+1] = tmp3[i]
    for i in range(h-1):
        tmp_lst[i][w-1] = tmp4[i] 
    
else:
    tmp1 = tmp_lst[0][:-1]
    tmp3 = tmp_lst[h-1][1:]
    tmp2 = []
    tmp4 = []
    for i in range(h-1):
        tmp2.append(tmp_lst[i+1][0])
        tmp4.append(tmp_lst[i][w-1])
    for i in range(w-1):
        tmp_lst[0][i+1] = tmp1[i]
    for i in range(h-1):
        tmp_lst[i][0] = tmp2[i]
    for i in range(w-1):
        tmp_lst[h-1][i] = tmp3[i]
    for i in range(h-1):
        tmp_lst[i+1][w-1] = tmp4[i]    
        
tmpx = stpx-1-rdown
tmpy = stpy-1-rdown
for j in range(lup+1):  # tmp_lst y 좌표
    for k in range(rup+1):  # tmp_lst x 좌표
        lst[tmpy - k][tmpx + k] = tmp_lst[j][k]
    tmpx += 1
    tmpy += 1

for arr in lst:
    print(*arr, sep=' ')