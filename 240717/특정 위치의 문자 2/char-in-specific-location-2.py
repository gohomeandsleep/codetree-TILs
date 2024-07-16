lst = list(input().split(' '))

for i in range(len(lst)):
    if i % 3 == 1:
        print(lst[i], end=' ')