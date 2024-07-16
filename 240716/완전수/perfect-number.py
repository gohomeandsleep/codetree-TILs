stp, endp = map(int, input().split())

lst = [6, 28, 496]

cnt = 0
for i in range(stp, endp+1):
    if i in lst:
        cnt += 1
print(cnt)