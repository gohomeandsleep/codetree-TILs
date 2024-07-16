n = int(input())

for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(n- i // 2):
            print("*", end=' ')
    else:
        for j in range(i // 2):
            print("*", end=' ')
    print('')

for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(n // 2 - i // 2):
            print("*", end=' ')
    else:
        for j in range(i // 2 + n // 2):
            print("*", end=' ')
    print('')