n, q = map(int , input().split())
lst = list(map(int, input().split()))

for _ in range(q):
    inst = list(map(int, input().split()))
    if inst[0] == 1:
        print(lst[inst[1]-1])
    elif inst[0] == 2:
        try:
            print(lst.index(inst[1]) + 1)
        except:
            print(0)
    elif inst[0] == 3:
        for i in range(inst[1]-1, inst[2] ):
            print(lst[i], end=' ')
        print('')