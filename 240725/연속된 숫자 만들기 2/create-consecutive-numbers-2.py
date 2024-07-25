lst = list(map(int, input().split()))
lst.sort()

if lst[0] + 1 == lst[1] and lst[1] + 1 == lst[2]:
    print(0)
elif lst[1] - lst[0] <= 2 or lst[2] - lst[1] <= 2:
    print(1)
else:
    print(2)