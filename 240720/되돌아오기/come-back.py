T = int(input())

x, y, cnt, stat= 0, 0, 1, 0
direct = ['E', 'W', 'N', 'S']
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(T):
    d, l = input().split()
    idx_d = direct.index(d)
    for i in range(int(l)):
        x += dx[idx_d]
        y += dy[idx_d]
        if x == 0 and y == 0:
            stat = 1
            print(cnt)
            break
        cnt += 1
if stat == 0:
    print(-1)