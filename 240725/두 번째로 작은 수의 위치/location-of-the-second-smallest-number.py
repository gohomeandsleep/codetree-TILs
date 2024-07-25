n = int(input())
lst = list(map(int, input().split()))

tmp = lst[:]
smallest = min(tmp)
for i in range(n):
    #print(i)
    if tmp[i] == smallest:
        tmp[i] = 100
#print(tmp)
second = min(tmp)

if lst.count(second) >= 2 or lst.count(second) == 0:
    print(-1)
else:
    print(lst.index(second) + 1)