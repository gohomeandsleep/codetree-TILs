n, k = map(int, input().split())
order = list(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y, d = n // 2, n // 2, 0
score = lst[n // 2][n // 2]
for i in range(len(order)):
    if order[i] == 'R':
        d = (d + 1) % 4
    elif order[i] == 'L':
        d = (d - 1) % 4
    else:
        if 0 <= x+dx[d] < n and 0 <= y+dy[d] < n:
            x += dx[d]
            y += dy[d]
            score += lst[y][x]
            #print(score)

print(score)