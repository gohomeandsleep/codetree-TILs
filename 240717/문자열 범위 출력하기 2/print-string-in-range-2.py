lst = list(input())
n = int(input())
if len(lst) > n:
    lst = lst[len(lst) - n:]
lst = lst[::-1]
print(*lst, sep='')