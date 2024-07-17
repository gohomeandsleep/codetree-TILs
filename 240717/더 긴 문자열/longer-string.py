a, b = list(input().split())

if len(a) > len(b):
    print(*a, sep='', end=' ')
    print(len(a))
elif len(a) < len(b):
    print(*b, sep='', end=' ')
    print(len(b))
else:
    print('same')