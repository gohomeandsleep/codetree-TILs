a, b = map(int, input().split())

while b >= a:
    if a % 2 == 0:
        print(a, end=' ')
    a += 1