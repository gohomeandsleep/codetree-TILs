n = int(input())
lst = list(map(int, input().split()))

for i in lst:
    if i % 2 == 0:
        print(i // 2, end=' ')
    else:
        print(i, end=' ')