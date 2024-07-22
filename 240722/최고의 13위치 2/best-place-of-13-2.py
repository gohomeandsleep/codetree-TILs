n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
first = 0
second = 0
third = 0
for y in range(n):
    prev_x = 0
    for x in range(n-2):
        tmp = lst[y][x] + lst[y][x+1] + lst[y][x+2]
        if tmp >= first:
            third = second
            second = first
            first = tmp
            #print(x, prev_x, end="|\n")
            if x <= prev_x:
                second = third
            prev_x = x + 2
            #print(prev_x)
        elif tmp >= second:
            third = second
            second = tmp
            if x <= prev_x:
                second = third
           
        #print(first, second) 
print(first + second)