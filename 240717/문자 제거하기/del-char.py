lst = list(input())
for _ in range(len(lst)-1):
    n = int(input())
    if n >= len(lst):
        lst.pop(-1)
    else:
        lst.pop(n)
    print(*lst, sep='')