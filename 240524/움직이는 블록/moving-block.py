n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

avg = sum(lst) // n
res = 0
for num in lst:
    if num > avg:
        res += num - avg

print(res)