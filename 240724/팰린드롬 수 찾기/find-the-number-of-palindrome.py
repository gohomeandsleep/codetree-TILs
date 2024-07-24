stp, endp = map(int, input().split())

res = 0
for i in range(stp, endp + 1):
    tmp = list(str(i))
    stat = True
    for i in range(len(tmp) // 2):
        if tmp[i] != tmp[len(tmp) - i - 1]:
            stat = False
    if stat == True:
        res += 1

print(res)