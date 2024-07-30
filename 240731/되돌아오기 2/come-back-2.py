x, y, cnt, stat, d= 0, 0, 1, 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
lst = list(input())
for i in range(len(lst)):
    if lst[i] == 'F':
        x += dx[d]
        y += dy[d]
    if lst[i] == 'R':
        d = (d + 1) % 4
    if lst[i] == 'L':
        d = (d - 1) % 4

    if x == 0 and y == 0:
        stat = 1
        print(cnt)
        break
    cnt += 1

if stat == 0:
    print(-1)