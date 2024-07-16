lst = list(input())

for i in range(1, len(lst)+1):
    if i % 3 == 2:
        print(lst[i], end='')