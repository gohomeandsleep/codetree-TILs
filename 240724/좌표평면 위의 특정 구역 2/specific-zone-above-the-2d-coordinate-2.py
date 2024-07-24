n = int(input())
xlst = []
ylst = []
for _ in range(n):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)
res = float('inf')
for i in range(n):
    tmpx = xlst.pop(0)
    tmpy = ylst.pop(0)
    res = min(res, (max(xlst) - min(xlst)) * (max(ylst) - min(ylst)))
    xlst.append(tmpx)
    ylst.append(tmpy)
print(res)