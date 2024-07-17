lst = list(input())

print(*lst, sep='')
for _ in range(len(lst)):
    tmp = lst.pop(-1)
    lst = list(tmp) + lst
    print(*lst, sep='')