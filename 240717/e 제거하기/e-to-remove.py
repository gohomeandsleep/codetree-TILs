lst = list(input())
e = 'e'

for i in range(len(lst)):
    if lst[i] == e:
        lst.pop(i)
        break

print(*lst, sep='')