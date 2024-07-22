n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k and abs(j - l) <= 2: 
                    continue
                else:
                    cnt1 = lst[i][j] + lst[i][j+1] + lst[i][j+2]
                    cnt2 = lst[k][l] + lst[k][l+1] + lst[k][l+2]
                    cnt = max(cnt, cnt1 + cnt2)


print(cnt)