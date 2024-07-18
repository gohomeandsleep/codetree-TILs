lst = list(input())

res = 0
for i in range(len(lst)):
    res += int(lst[i]) ** 2

print(res)