n = int(input())

for i in range(n):
    for j in range(1, n+1):
        print(n * i + j, end=' ')
    print('')