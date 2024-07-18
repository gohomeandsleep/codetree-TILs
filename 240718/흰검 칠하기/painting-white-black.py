n = int(input())
lst = [' ' for _ in range(200000)]
num = [0 for _ in range(200000)]

cur = 100000
for _ in range(n):
    l, d = input().split()
    if d == 'R':
        for i in range(cur, cur + int(l)):
            lst[i] = 'B'
            num[i] += 1
            cur += 1
    else:
        for i in range(cur-1, cur - int(l) -1, -1):
            lst[i] = 'W'
            num[i] += 1
            cur -= 1
    #print(cur)

black = 0
grey = 0
white = 0
res = 0
for i in range(200000):
    if num[i] >= 4:
        grey += 1
    elif lst[i] == 'B':
        black += 1
    elif lst[i] == 'W':
        white += 1
print(white, black, grey)