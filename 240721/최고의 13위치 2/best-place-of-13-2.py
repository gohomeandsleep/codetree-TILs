n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
first = 0
second = 0
for y in range(n):
    for x in range(n-2):
        tmp = lst[y][x] + lst[y][x+1] + lst[y][x+2]
        if tmp > first:
            second = first
            first = tmp
        elif tmp > second:
            second = tmp
print(first + second)