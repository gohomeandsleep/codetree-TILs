lst, T = input().split()
lst = list(lst)
for _ in range(int(T)):
    inst = list(input().split())
    if inst[0] == '1':
        a = int(inst[1])-1
        b = int(inst[2])-1
        lst[a], lst[b] = lst[b], lst[a]
        print(*lst, sep='')
    elif inst[0] == '2':
        a = inst[1]
        b = inst[2]
        for i in range(len(lst)):
            if lst[i] == a:
                lst[i] = b
        print(*lst, sep='')