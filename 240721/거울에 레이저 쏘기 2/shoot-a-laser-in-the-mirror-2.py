#import time
n = int(input())
lst = [list(input()) for _ in range(n)]
k = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

if k <= n:
    d = 2
    x = k - 1
    y = 0
elif k <= 2 * n:
    d = 3
    y = k - n - 1
    x = n - 1
elif k <= 3 * n:
    d = 0
    y = n - 1
    x = 3 * n - k
elif k <= 4 * n:
    d = 1
    x = 0
    y = 4 * n - k

cnt = 1
prev = []
while True:
    if lst[y][x] == '/':
        if d % 2 == 0:
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        x += dx[d]
        y += dy[d]
        if x < 0 or y < 0 or x > n or y > n:
            break
        else:
            try:
                prev.append(lst[y][x])
            except:
                break
        cnt += 1
        
    else:
        if d % 2 == 0:
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        x += dx[d]
        y += dy[d]
        if x < 0 or y < 0 or x > n or y > n:
            break
        else:
            try:
                prev.append(lst[y][x])
            except:
                break
        cnt += 1
        
    #print(d, y, x, prev)
    #time.sleep(1)

print(cnt)