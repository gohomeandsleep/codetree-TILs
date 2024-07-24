stp, endp = map(int, input().split())

mxm = 0
for i in range(stp, endp + 1):
    tmp = list(str(i))
    cnt = 0
    for j in range(len(tmp)):
        cnt += int(tmp[j])
    mxm = max(mxm, cnt)
print(mxm)