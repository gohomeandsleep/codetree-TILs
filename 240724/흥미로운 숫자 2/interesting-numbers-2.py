stp, endp = map(int, input().split())

res = 0
for i in range(stp, endp + 1):
    tmp = list(str(i))
    tmp.sort()
    if tmp.count(tmp[0]) == 1:
        if tmp.count(tmp[-1]) == len(tmp) - 1:
            res += 1
    else:
        if tmp.count(tmp[-1]) == 1:
            res += 1

print(res)