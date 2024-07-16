n = int(input())

x = 64
for i in range(n):
    for j in range(n):
        x += 1
        print(chr(x), end='')
    print('')