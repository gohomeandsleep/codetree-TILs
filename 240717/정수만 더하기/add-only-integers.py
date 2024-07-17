lst = list(input())
res = 0
for i in range(len(lst)):
    if ord(lst[i]) >= 48 and ord(lst[i]) <= 57:
        res += int(lst[i])
print(res)