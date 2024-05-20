n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

dxs = [0,0,1,-1]
dys = [1,-1,0,0]

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x = i + dx
            y = j + dy
            if not(0<=x < n and 0 <=y <n):
                continue
            cnt += num_list[x][y]
        if cnt >= 3:
            ans +=1

print(ans)