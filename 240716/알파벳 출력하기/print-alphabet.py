n = int(input())

x = 64
for i in range(1, n+1):
    for j in range(i):
        x += 1
        if x > 90:
            x -= 26
        print(chr(x), end='')
    print('')