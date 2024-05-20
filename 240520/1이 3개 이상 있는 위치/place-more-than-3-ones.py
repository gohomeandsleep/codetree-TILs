n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

res = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            try:
                cnt += num_list[i+dxs[k]][j+dys[k]]
            except:
                cnt += 0
        if cnt >= 3:
            res += 1

print(res)