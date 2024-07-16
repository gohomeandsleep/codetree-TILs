n = int(input())

x = 64
for i in range(1, n+1):
    for j in range(i-1):
        print("  ", end='')
    for j in range(n-i, -1, -1):
        x += 1
        if x > 90:
            x -= 26
        print(chr(x), end=' ')
    print('')