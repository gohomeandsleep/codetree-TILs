n, m = map(int, input().split())
a, b = map(int, input().split())

lst = [0 for _ in range(101)]
for i in range(n+1, m+1):
    lst[i] = 1

for i in range(a+1, b+1):
    lst[i] = 1

print(sum(lst))