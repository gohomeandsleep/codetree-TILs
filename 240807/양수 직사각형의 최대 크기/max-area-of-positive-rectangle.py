n, m = map(int, input().split()) #n:세로, m:가로
lst = [list(map(int, input().split())) for _ in range(n)]

res = -1
for stpy in range(n):
    for endy in range(stpy+1, n+1):
        for stpx in range(m):
            for endx in range(stpx+1, m+1):
                cnt = 0
                check = True
                for i in range(stpy, endy):
                    for j in range(stpx, endx):
                        if lst[i][j] <= 0: check = False
                        else: cnt += 1
                if check == True: res = max(res, cnt)
print(res)