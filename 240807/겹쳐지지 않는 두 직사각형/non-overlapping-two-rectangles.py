def rect(x1, y1, x2, y2):
    tmp = 0
    for i in range(y1, y2):
        for j in range(x1, x2):
            tmp += lst[i][j]
    return tmp

n, m = map(int, input().split())  # n: 세로, m: 가로
lst = [list(map(int, input().split())) for _ in range(n)]

res = -10000000
stat = False
for stpy in range(n):
    for endy in range(stpy + 1, n + 1):
        for stpx in range(m):
            for endx in range(stpx + 1, m + 1):
                for stpy2 in range(n):
                    for endy2 in range(stpy2 + 1, n + 1):
                        for stpx2 in range(m):
                            for endx2 in range(stpx2 + 1, m + 1):
                                # 두 직사각형이 겹치지 않도록 조건 수정
                                if endy <= stpy2 or endx <= stpx2:
                                    stat = True
                                    p_sum = rect(stpx, stpy, endx, endy) + rect(stpx2, stpy2, endx2, endy2)
                                    res = max(res, p_sum)
                                    
print(res)