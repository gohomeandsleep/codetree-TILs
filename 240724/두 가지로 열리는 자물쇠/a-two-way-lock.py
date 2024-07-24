n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

res = 1
for i in range(3):
    dist = min(abs(lst1[i] - lst2[i]), abs(min(lst1[i], lst2[i]) - max(lst1[i], lst2[i])))
    if dist < 5:
        res *= (5 - dist)
    else:
        res = 0

if n <= 4:
    print(n ** 3)
else:
    print(250 - res)