n = int(input())
lst = list(input().split())

res = 0
for i in range(n):
    for j in range(n-i-1):
        #print(lst[i], lst[j])
        if ord(lst[j]) > ord(lst[j+1]):
            lst[j+1], lst[j] = lst[j], lst[j+1]
            res += 1
print(res)