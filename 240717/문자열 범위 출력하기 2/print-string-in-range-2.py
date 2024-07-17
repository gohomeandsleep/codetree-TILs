lst = list(input())
n = int(input())

lst = lst[len(lst) - n:]
lst = lst[::-1]
print(*lst, sep='')