stp, endp = map(int, input().split())
lst = ['3', '6', '9']

res = 0
for i in range(stp, endp+1):
    tmp = list(str(i))
    if lst[0] in tmp or lst[1] in tmp or lst[2] in tmp:
       res += 1
    elif i % 3 == 0:
        res += 1

print(res)