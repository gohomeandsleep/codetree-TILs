n = int(input())
lst = []

for _ in range(n):
    inst = list(input().split())
    if inst[0] == 'push':
        lst.append(inst[1])
    elif inst[0] == 'pop':
        print(lst[-1])
        lst.pop(-1)
    elif inst[0] == 'size':
        print(len(lst))
    elif inst[0] == 'empty':
        if len(lst) == 0: print(1)
        else: print(0)
    elif inst[0] == 'top':
        print(lst[-1])