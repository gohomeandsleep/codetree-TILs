n = int(input())
lst = [int(input()) for _ in range(n)]

res = 0
for i in lst:
    if i % 3 == 0 and i % 2 == 1:
       res += i

print(res)