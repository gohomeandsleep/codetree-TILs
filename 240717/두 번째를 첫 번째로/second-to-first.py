lst = list(input())
a = lst[0]
b = lst[1]
for i in range(len(lst)):
    if lst[i] == b:
        lst[i] = a

print(*lst, sep='')