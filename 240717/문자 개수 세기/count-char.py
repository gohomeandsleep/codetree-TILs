lst = list(input())
c = input()

res = 0
for i in range(len(lst)):
    if lst[i] == c:
        res += 1

print(res)