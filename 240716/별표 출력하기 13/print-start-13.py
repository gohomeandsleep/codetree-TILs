n = int(input())

for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(n- i // 2):
            print("*", end=' ')
    else:
        for j in range(i // 2):
            print("*", end=' ')
    print('')

if n % 2 == 0:
    for i in range(1, n+1):
        if i % 2 == 0:
            for j in range((n + i) // 2):
                print("*", end=' ')
        else:
            for j in range((n-i+1) // 2):
                print("*", end=' ')
        print('')
else:
    for i in range(1, n+1):
        if i % 2 == 0:
            for j in range((n - i + 1) // 2):
                print("*", end=' ')
        else:
            for j in range((n + i) // 2):
                print("*", end=' ')
        print('')