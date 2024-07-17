n = int(input())
lst = list(input())

res = 1
for i in range(len(lst)):
    if lst[i] != ' ':
        print(lst[i], end='')
        if res % 5 == 0:
            print('')
        res += 1