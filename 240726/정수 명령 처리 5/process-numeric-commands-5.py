n = int(input())
lst = []
for _ in range(n):
    inst = list(input().split())
    if inst[0] == 'push_back':
        lst.append(inst[1])
    elif inst[0] == 'get':
        print(lst[int(inst[1]) - 1])
    elif inst[0] == 'pop_back':
        lst.pop(-1)
    elif inst[0] == 'size':
        print(len(lst))