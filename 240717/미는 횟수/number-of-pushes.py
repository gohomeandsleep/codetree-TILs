lst1 = list(input())
lst2 = list(input())

cnt = 0
while True:
    tmp = lst1.pop(-1)
    lst1 = list(tmp) + lst1
    if lst1 == lst2:
        print(cnt+1)
        break
    cnt += 1
    if cnt >= len(lst1):
        break