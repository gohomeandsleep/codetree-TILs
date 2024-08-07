n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

def in_range(y, x):
    return 0 <= x < n and 0 <= y < n and lst[y][x] != 0

res = 0
if n % 2 == 0:  # n이 짝수일 때는 첫 줄 탐색만으로 가장 큰 값을 알 수 있다.
    for i in range(1, n-1):
        direction = 0
        p_sum = 0
        tmpx, tmpy = i, 0
        while direction < 4:
            if in_range(tmpy + dy[direction], tmpx + dx[direction]):
                tmpx += dx[direction]
                tmpy += dy[direction]
                p_sum += lst[tmpy][tmpx]
            else:
                direction += 1
        res = max(res, p_sum)
else:
    """
    n이 홀수일 때는 첫 줄 탐색만으로 가장 큰 값을 알 수 없다.
    중심을 통과하는 수 중 가장 큰 값을 탐색해야 함
    """
    for i in range(1, n-1):
        direction = 0
        p_sum = 0
        tmpx, tmpy = i, 0
        while direction < 4:
            if in_range(tmpy + dy[direction], tmpx + dx[direction]):
                tmpx += dx[direction]
                tmpy += dy[direction]
                p_sum += lst[tmpy][tmpx]
            else:
                direction += 1
        res = max(res, p_sum)
    
print(res)