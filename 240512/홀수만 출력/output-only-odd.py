stp, endp = map(int, input().split())

if stp % 2 == 0:
    stp += 1

for i in range(stp, endp+1, 2):
    print(i, end=' ')