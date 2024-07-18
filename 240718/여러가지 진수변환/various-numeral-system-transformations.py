n, b = map(int, input().split())
lst = []
if b == 4:
    for i in range(4, -1, -1):
        if n // 4 ** i != 0:
            lst.append(n // 4 ** i)
            n -= lst[-1] * 4 ** i
        elif len(lst) != 0:
            lst.append(0)
    print(*lst, sep='')
if b == 8:
    for i in range(3, -1, -1):
        if n // 8 ** i != 0:
            lst.append(n // 8 ** i)
            n -= lst[-1] * 8 ** i
        elif len(lst) != 0:
            lst.append(0)
    print(*lst, sep='')