n, k = map(int, input().split())
lst = []
bomb = []
for i in range(n):
    tmp = int(input())
    if tmp in lst:
        bomb.append(tmp)
    lst.append(tmp)
try:
    print(max(bomb))
except:
    print(-1)