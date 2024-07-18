n = int(input())
lst = list(map(int, input().split()))
slst = lst
slst = sorted(slst)

for i in range(n):
    print(slst.index(lst[i]) + lst[:i].count(lst[i]) + 1, end=' ')