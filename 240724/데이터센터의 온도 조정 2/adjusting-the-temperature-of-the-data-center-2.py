n, c, g, h = map(int, input().split())
lst = []
end = 0
for _ in range(n):
    Ta, Tb = map(int, input().split())
    end = max(end, Tb)
    lst.append([Ta, Tb])

mxm = 0
for i in range(1, end + 2):
    tmp = 0
    for j in range(n):
        if i < lst[j][0]:
            tmp += c
        elif i <= lst[j][1]:
            tmp += g
        else:
            tmp += h
    mxm = max(mxm, tmp)

print(mxm)