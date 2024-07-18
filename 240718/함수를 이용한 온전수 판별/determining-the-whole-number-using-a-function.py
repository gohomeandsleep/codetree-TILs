stp, endp = map(int, input().split())

cnt = 0
for i in range(stp, endp+1):
    if i % 2 == 0:
        continue
    elif i % 10 == 5:
        continue
    elif i % 3 == 0 and i % 9 != 0:
        continue
    else:
        cnt += 1

print(cnt)