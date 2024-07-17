lst = [list(input()) for _ in range(10)]
c = input()

for i in range(10):
    if lst[i][-1] == c:
        print(*lst[i], sep='')