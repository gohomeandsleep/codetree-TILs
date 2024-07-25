n = int(input())
up = 0
down = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        if b == 2:
            up += 1
        elif b == 3:
            down += 1
    elif a == 2:
        if b == 3:
            up += 1
        elif b == 1:
            down += 1
    elif a == 3:
        if b == 1:
            up += 1
        elif b == 2:
            down += 1
print(max(up, down))