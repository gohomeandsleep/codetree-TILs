n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 0
for y in range(n):
    for x in range(n):
        cnt = 0
        for i in range(4):
            if 0 <= y+dy[i] < n and 0<= x+dx[i] < n and lst[y+dy[i]][x+dx[i]] == 1:
                cnt += 1
        if cnt >= 3: res += 1
print(res)