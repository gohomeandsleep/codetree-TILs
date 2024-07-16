n = int(input())

for i in range(1, 2*n + 2):
    if i % 2 != 0:
        for j in range(2*n+1):
            print("*", end=' ')
    else:
        for j in range(n + 1):
            print("*  ", end=' ')
    print('')