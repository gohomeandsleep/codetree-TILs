lst = list(input())

lst.sort()

if lst[0] != lst[-1]:
    print('Yes')
else:
    print('No')