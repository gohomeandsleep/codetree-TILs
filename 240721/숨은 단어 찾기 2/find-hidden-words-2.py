n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

tar = ['L', 'E', 'E']
tar_r = ['E', 'E', 'L']

cnt = 0
for y in range(n):
    for x in range(m):
        if y + 2 < n:
            tmp = [lst[y][x], lst[y+1][x], lst[y+2][x]]
            if tmp == tar or tmp == tar_r:
                cnt += 1
        if x + 2 < m:
            tmp = [lst[y][x], lst[y][x+1], lst[y][x+2]]
            if tmp == tar or tmp == tar_r:
                cnt += 1
        if x + 2 < m and y + 2 < n:
            tmp = [lst[y][x], lst[y+1][x+1], lst[y+2][x+2]]
            if tmp == tar or tmp == tar_r:
                cnt += 1
        if x + 2 < m and y - 2 >= 0:
            tmp = [lst[y][x], lst[y-1][x+1], lst[y-2][x+2]]
            if tmp == tar or tmp == tar_r:
                cnt += 1
print(cnt)