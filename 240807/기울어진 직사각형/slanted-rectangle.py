n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

def in_range(y, x):
    return 0 <= x < n and 0 <= y < n

res = 0
if n % 2 == 0: #n이 짝수일때는 첫 줄 탐색만으로 가장 큰 값을 알 수 있다.
    for i in range(1, n-1):
        direction = 0
        p_sum = 0
        tmpx, tmpy = i, 0
        while direction < 4:
            if in_range(tmpy+dy[direction], tmpx+dx[direction]):
                tmpx += dx[direction]
                tmpy += dy[direction]
                p_sum += lst[tmpy][tmpx]
            else:
                direction += 1
        res = max(res, p_sum)
else:
    for i in range(1, n-1):
        direction = 0
        p_sum = 0
        tmpx, tmpy = i, 0
        while direction < 4:
            if in_range(tmpy+dy[direction], tmpx+dx[direction]):
                tmpx += dx[direction]
                tmpy += dy[direction]
                p_sum += lst[tmpy][tmpx]
            else:
                direction += 1
        res = max(res, p_sum)
print(p_sum)