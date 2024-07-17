lst = list(input())
c = list(input())

stat = True
for i in range(len(lst) - len(c) + 1):
    if lst[i:i+len(c)] == c:
        stat = False
        print(i)
        break

if stat == True:
    print(-1)