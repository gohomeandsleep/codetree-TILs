lst = list(input())
part = list(input())

res = False
for i in range(len(lst) - len(part) + 1):
    if lst[i:i+len(part)] == part:
        res = True
        print(i)

if res == False:
    print(-1)