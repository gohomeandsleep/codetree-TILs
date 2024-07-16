n = int(input())

for i in range(11, 11 + n * 2, 2):
    for j in range(n):
        print(i + 2 * j, end=' ')
    print('')