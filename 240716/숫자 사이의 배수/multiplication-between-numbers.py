n, m = map(int, input().split())

lst = []
for i in range(n, m+1):
    if i % 5 == 0 or i % 7 == 0:
        lst.append(i)

print(sum(lst), end=' ')
print("%.1f" % (sum(lst) / len(lst)))