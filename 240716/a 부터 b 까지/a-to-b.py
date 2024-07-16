a, b = map(int, input().split())
print(a, end=' ')
while a < b:
    if a % 2 == 0:
        a += 3
        print(a, end=' ')
    else:
        a *= 2
        print(a, end=' ')