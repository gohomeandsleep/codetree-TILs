lst = list(input())

for i in range(len(lst)-1, -1, -1):
    if i % 2 != 0:
        print(lst[i], end='')