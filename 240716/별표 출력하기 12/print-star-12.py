n = int(input())

for i in range(n):
    print("* ", end='')
print('')

if n % 2 == 0:
    for i in range(1, n):
        for j in range((i) // 2):
            print("    ", end='')
        for j in range((n-i-1) // 2 + 1):
            print("  *", end=' ')
        print('')
else:
    for i in range(1, n):
        for j in range((i) // 2):
            print("    ", end='')
        for j in range((n-i-2) // 2 + 1):
            print("  *", end=' ')
        print('')