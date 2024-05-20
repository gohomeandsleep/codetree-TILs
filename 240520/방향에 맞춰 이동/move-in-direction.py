n = int(input())

x,y = 0, 0
for _ in range(n):
    dir, num = input().split()
    if dir == 'N':
        y += int(num)
    if dir == 'S':
        y -= int(num)
    if dir == 'E':
        x += int(num)
    if dir == 'W':
        x -= int(num)

print(x, y)