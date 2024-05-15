a1, a2 = map(int, input().split())

print(a1, a2, end=' ')
for i in range(8):
    a3 = a2 + 2*a1
    print(a3, end=' ')
    a1 = a2
    a2 = a3