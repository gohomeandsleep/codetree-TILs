lst = [list(input()) for _ in range(10)]
c = input()

res = True
for i in range(10):
    if lst[i][-1] == c:
        res = False
        print(*lst[i], sep='')
if res == False:
    print("None")