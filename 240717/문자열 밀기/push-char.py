lst = list(input())

lst.append(lst.pop(0))
print(*lst, sep='')