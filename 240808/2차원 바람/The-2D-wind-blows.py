n, m, q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
inst = [list(map(int, input().split())) for _ in range(q)]

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 1, -1, 0]

def in_range(y, x):
    return 0 <= x < m and 0 <= y < n

def calculate_average(y, x):
    cnt = 0
    p_sum = 0
    for k in range(5):
        ny, nx = y + dy[k], x + dx[k]
        if in_range(ny, nx):
            p_sum += lst[ny][nx]
            cnt += 1
    return int(p_sum / cnt)

for i in range(q):
    stpy = inst[i][0] - 1
    stpx = inst[i][1] - 1
    endy = inst[i][2] - 1
    endx = inst[i][3] - 1
    tmp1 = lst[stpy][stpx:endx]
    tmp2 = []
    for j in range(stpy, endy):
        tmp2.append(lst[j][endx])
    tmp4 = []
    for j in range(stpy+1, endy+1):
        tmp4.append(lst[j][stpx])
    tmp3 = lst[endy][stpx+1:endx+1]

    for j in range(len(tmp1)):
        lst[stpy][stpx+j+1] = tmp1[j]
    for j in range(len(tmp3)):
        lst[endy][stpx+j] = tmp3[j]
    for j in range(len(tmp2)):
        lst[stpy+j+1][endx] = tmp2[j]
    for j in range(len(tmp4)):
        lst[stpy+j][stpx] = tmp4[j]
    new_arr = [[0 for _ in range(endx-stpx+1)] for _ in range(endy-stpy+1)]
    for y in range(endy-stpy+1):
        for x in range(endx-stpx+1):
            new_arr[y][x] = calculate_average(stpy+y, stpx+x)    
    for y in range(endy-stpy+1):
        for x in range(endx-stpx+1):
            lst[stpy+y][stpx+x] = new_arr[y][x]

for arr in lst:
    print(*arr, sep=' ')