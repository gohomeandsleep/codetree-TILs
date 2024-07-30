n = int(input())
lst = [list(input()) for _ in range(n)]
k = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 시작 좌표와 방향 설정 함수
def set_start(n, k):
    if k <= n:
        return k - 1, 0, 2
    elif k <= 2 * n:
        return n - 1, k - n - 1, 3
    elif k <= 3 * n:
        return 3 * n - k, n - 1, 0
    else:
        return 0, 4 * n - k, 1

x, y, d = set_start(n, k)
cnt = 0

# 방향 전환 함수
def change_direction(current_direction, char):
    if char == '/':
        return (current_direction + 1) % 4 if current_direction % 2 == 0 else (current_direction - 1) % 4
    else:  # char == '\'
        return (current_direction - 1) % 4 if current_direction % 2 == 0 else (current_direction + 1) % 4

# 이동 및 경계 검사
while 0 <= x < n and 0 <= y < n:
    cnt += 1
    d = change_direction(d, lst[y][x])
    x += dx[d]
    y += dy[d]

print(cnt)