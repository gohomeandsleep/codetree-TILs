n, m = map(int, input().split())

print(n, m, end=' ')

for i in range(4):
    if n + m >= 10:
        n = n + m - 10
        print(n, end=' ')
    else:
        n = n + m
        print(n, end=' ')
    
    if n + m >= 10:
        m = n + m - 10
        print(m, end=' ')
    else:
        m = n + m
        print(m, end=' ')