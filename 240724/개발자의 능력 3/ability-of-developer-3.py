lst = list(map(int, input().split()))
lst.sort(reverse=True)

a = [0]
b = [0]
for i in range(6):
    if sum(a) >= sum(b):
        b.append(lst[i])
    else:
        a.append(lst[i])

print(abs(sum(a) - sum(b)))