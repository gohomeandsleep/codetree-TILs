end = ['E', 'N', 'D']
while True:
    lst = list(input())
    if lst == end:
        break
    else:
        print(*lst[::-1], sep='')