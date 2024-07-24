import itertools

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lstc = list(itertools.combinations(lst, n - 3))

res = 0
for single in lstc:
    single = list(single)
    tmp = []
    stat = True
    for i in range(len(single)):
        for j in range(single[i][0], single[i][1] + 1):
            if j in tmp:
                stat = False
            else:
                tmp.append(j)
    if stat == True:
        res += 1
print(res)