n = int(input())
lst = [[] for _ in range(200000)]

cur = 100000
for _ in range(n):
    l, d = input().split()
    if d == 'R':
        for i in range(cur, cur + int(l)):
            lst[i].append('B')
        cur += int(l)-1
    else:
        for i in range(cur, cur - int(l), -1):
            lst[i].append('W')
        cur -= int(l)-1
    #print(cur)

black = 0
grey = 0
white = 0
for i in range(200000):
    if lst[i] and lst[i][-1] == 'B':
        black += 1
    elif lst[i] and lst[i][-1] == 'W':
        white += 1
print(white, black)