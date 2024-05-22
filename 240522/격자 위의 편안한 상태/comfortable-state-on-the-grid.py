n, m = map(int, input().split())

lst = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m):
    r, c = map(int, input().split())
    lst[r-1][c-1] = 1


    cnt = 0
    for i in range(4):
        try:
            if r-1-dx[i] < 0 or c-1+dy[i] < 0:
                continue
            elif lst[r-1+dx[i]][c-1+dy[i]] == 1:
                cnt += 1
        except:
            cnt += 0
    if cnt == 3:
        print(1)
    else:
        print(0)