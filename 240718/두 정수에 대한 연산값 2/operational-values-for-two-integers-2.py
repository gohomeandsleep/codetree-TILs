a, b = map(int, input().split())

if a < b:
    print(a + 10, b * 2)
else:
    print(a * 2, b + 10)