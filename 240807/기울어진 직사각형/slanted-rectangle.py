n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(1, n-1):  # y 시작 좌표
    tmp_lst = [[0 for _ in range(i + 1)] for _ in range(n - i)]
    tmpx = 0
    tmpy = i
    for j in range(n - i):  # tmp_lst y 좌표
        for k in range(i + 1):  # tmp_lst x 좌표
            if tmpy - k >= 0 and tmpx + k < n:
                tmp_lst[j][k] = lst[tmpy - k][tmpx + k]
        tmpx += 1
        tmpy += 1
    for stpy in range(n - i):
        for endy in range(stpy, n - i):
            for stpx in range(i + 1):
                for endx in range(stpx, i + 1):
                    tmp_v = 0
                    for k in range(stpy, endy + 1):
                        for l in range(stpx, endx + 1):
                            if k == stpy or k == endy or l == stpx or l == endx:
                                tmp_v += tmp_lst[k][l]
                    res = max(res, tmp_v)

print(res)