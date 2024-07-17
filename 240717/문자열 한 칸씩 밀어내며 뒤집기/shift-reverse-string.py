lst, n = input().split()
lst = list(lst)
for _ in range(int(n)):
    k = int(input())
    if k == 1:
        lst.append(lst.pop(0))
    elif k == 2:
        tmp = lst.pop(-1)
        lst = list(tmp) + lst
    else:
        lst = lst[::-1]
    print(*lst, sep='')