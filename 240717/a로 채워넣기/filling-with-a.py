lst = list(input())
lst[1] = 'a'
lst[-2] = 'a'
print(*lst, sep='')