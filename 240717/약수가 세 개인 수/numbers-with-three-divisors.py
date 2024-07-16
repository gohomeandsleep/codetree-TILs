stp, endp = map(int, input().split())

lst = [2,3,5,7,11,13,17,19,23,29,31]
mul = [i**2 for i in lst]

cnt = 0
for i in range(stp, endp+1):
    if i in mul:
        cnt += 1
print(cnt)