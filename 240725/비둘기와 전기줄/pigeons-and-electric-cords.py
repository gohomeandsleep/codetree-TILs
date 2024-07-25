n = int(input())
pigeon = [-1 for _ in range(10)]
cnt = 0
for _ in range(n):
    p, num = map(int, input().split())
    if pigeon[p-1] == -1:
        pigeon[p-1] = num
    else:
        if pigeon[p-1] != num:
            cnt += 1
            pigeon[p-1] = num
print(cnt)