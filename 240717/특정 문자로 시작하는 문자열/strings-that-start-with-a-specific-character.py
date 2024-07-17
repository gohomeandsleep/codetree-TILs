T = int(input())
lst = [list(input()) for _ in range(T)]
c = input()

res = []
for i in range(T):
    if lst[i][0] == c:
        res.append(len(lst[i]))

print(len(res), end=' ')
print("%.2f" % (sum(res) / len(res)))