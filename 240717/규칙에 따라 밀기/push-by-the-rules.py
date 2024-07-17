lst= list(input())
inst = list(input())
for i in range(len(inst)):
    if inst[i] == 'L':
        lst.append(lst.pop(0))
    elif inst[i] == 'R':
        tmp = lst.pop(-1)
        lst = list(tmp) + lst
print(*lst, sep='')