n = int(input())
lst = list(map(int, input().split()))

res = 0
for i in range(len(lst)):
    if lst[i] == 2:
        res+= 1
    if res == 3:
        print(i+1)
        break