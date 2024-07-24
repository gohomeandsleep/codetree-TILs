n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, 10001):
    stat = True
    k = i * 2
    for j in range(n):
        if lst[j][0] <= k <= lst[j][1]:
            k *= 2
        else:
            stat = False
    if stat == True:
        print(i)
        break