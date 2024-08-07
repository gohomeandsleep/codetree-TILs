n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n-2): #세로
    for j in range(n-2): #가로
        tmp = 0
        for k in range(3):
            tmp += sum(lst[i+k][j:j+3])
        res = max(res, tmp)

print(res)