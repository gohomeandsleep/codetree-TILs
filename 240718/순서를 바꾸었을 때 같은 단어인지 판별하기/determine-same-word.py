lst1 = list(input())
lst2 = list(input())

lst1.sort()
lst2.sort()

if lst1 == lst2:
    print('Yes')
else:
    print('No')