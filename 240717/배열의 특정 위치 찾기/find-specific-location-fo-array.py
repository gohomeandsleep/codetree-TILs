lst = list(map(int, input().split()))

res1 = []
res2 = []
for i in range(1, 11):
    if i % 2 == 0:
        res1.append(lst[i-1])
    if i % 3 == 0:
        res2.append(lst[i-1])

print(sum(res1), end=' ')
print("%.1f" % (sum(res2) / len(res2)))