n = int(input())
lst = [int(input()) for _ in range(n)]

print(sum(lst), end=' ')
print("%.1f" % (sum(lst) / len(lst)))