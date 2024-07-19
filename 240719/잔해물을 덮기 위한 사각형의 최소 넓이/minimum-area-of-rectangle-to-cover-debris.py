stpx1, stpy1, endpx1, endpy1 = map(int, input().split())
stpx2, stpy2, endpx2, endpy2 = map(int, input().split())

lst = [[-1] * 2001 for _ in range(2001)]
for i in range(1001 + stpy1, 1002 + endpy1):
    for j in range(1001 + stpx1, 1002 + endpx1):
        lst[i][j] = 1

for i in range(1002 + stpy2, 1001 + endpy2):
    for j in range(1002 + stpx2, 1001 + endpx2):
        lst[i][j] = 0

res = []
for i in range(2001):
    for j in range(2001):
        if lst[i][j] == 1:
            res.append([i, j])

xlst = [coord[0] for coord in res]
ylst = [coord[1] for coord in res]

try:
    #print((max(xlst) - min(xlst)) , (max(ylst) - min(ylst)))
    print((max(xlst) - min(xlst)) * (max(ylst) - min(ylst)))
except:
    print(0)