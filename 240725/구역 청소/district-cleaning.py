n, m = map(int, input().split())
a, b = map(int, input().split())

if n > a:
    n, a = a, n
    m, b = b, m

if m > a:
    print(m - n + b - a - m + a)
else:
    print(m - n + b - a)