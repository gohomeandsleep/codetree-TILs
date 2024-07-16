n = int(input())
res = [0 for _ in range(9)]
lst = list(map(int, input().split()))

for i in range(len(lst)):
    res[lst[i]-1] += 1

for i in range(9):
    print(res[i])