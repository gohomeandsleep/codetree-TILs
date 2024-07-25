n = int(input())
lst = list(input().split())

res = 0
for i in range(n):
    for j in range(n-i):
        #print(lst[i], lst[j])
        if ord(lst[i]) > ord(lst[j]):
            lst[i], lst[j] = lst[j], lst[i]
            res += 1
print(res)