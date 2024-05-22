n, m = map(int, input().split())

lst = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for _ in range(m):
    r, c = map(int, input().split())
    lst[r-1][c-1] = 1

    cnt = 0
    for i in range(4):
        nx, ny = r-1+dx[i], c-1+dy[i]
        if in_range(nx, ny) and lst[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)