n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse = True)

stat = False
for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        print(lst[i])
        stat = True
        break
if stat == False:
    print(-1)