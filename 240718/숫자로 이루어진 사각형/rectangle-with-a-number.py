n = int(input())
val = 0

for _ in range(n):
    for _ in range(n):
        if val > 8:
            val -= 8
        else:
            val += 1
        print(val, end=' ')
    print('')