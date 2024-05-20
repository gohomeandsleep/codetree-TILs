y_max, x_max = map(int, input().split())

def in_range(x, y):
    return 0<=x and x < x_max and 0 <= y and y < y_max

written_check = [[0 for _ in range(x_max)] for _ in range(y_max)]
result = [[0 for _ in range(x_max)] for _ in range(y_max)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x=0
y=0
direction = 0

for i in range(y_max * x_max):

    written_check[y][x] = 1
    result[y][x] = i+1

    next_x = x + dxs[direction]
    next_y = y + dys[direction]

    if not in_range(next_x, next_y) or written_check[next_y][next_x] == 1:
        direction = (direction + 1) % 4
        next_x = x + dxs[direction]
        next_y = y + dys[direction]

    x = next_x
    y = next_y

for i in range(y_max):
    print(*result[i])