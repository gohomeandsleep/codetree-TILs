n = int(input())
lst = list(map(int, input().split()))

res = 0
for i in range(n-1, 0, -1):
    #print(lst[i-1], lst[i], lst[i-1] > lst[i])
    if lst[i-1] > lst[i]:
        res = i
        break
print(res)