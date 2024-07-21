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
while x >= 0 and x < n and y >= 0 and y < n:
    if lst[y][x] == '/':
        if len(prev) >= 1 and prev[-1] == lst[y][x]:
            if len(prev) < 2 or prev[-2] != lst[y][x]:
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
        else:
            d = (d + 1) % 4
        x += dx[d]
        y += dy[d]
        try:
            prev.append(lst[y][x])
        except:
            break
        cnt += 1
        
    else:
        if len(prev) >= 1 and prev[-1] == lst[y][x]:
            if len(prev) < 2 or prev[-2] != lst[y][x]:
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
        else:
            d = (d - 1) % 4
        x += dx[d]
        y += dy[d]
        try:
            prev.append(lst[y][x])
        except:
            break
        cnt += 1
        
    #print(d, y, x, prev)
    #time.sleep(1)

print(cnt)