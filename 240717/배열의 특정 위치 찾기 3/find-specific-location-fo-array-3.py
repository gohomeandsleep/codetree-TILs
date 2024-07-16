lst = list(map(int, input().split()))

for i in range(len(lst)):
    if lst[i] == 0:
        print(sum(lst[i-3:i]))
        break