lst = [int(input()) for _ in range(10)]

res = []
for i in lst:
    if i >= 0 and i <= 200:
        res.append(i)

print(sum(res), end=' ')
print("%.1f" % (sum(res) / len(res)))