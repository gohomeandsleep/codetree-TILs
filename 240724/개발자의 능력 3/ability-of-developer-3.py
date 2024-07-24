lst = list(map(int, input().split()))
lst.sort(reverse=True)

a = [0]
b = [0]
for i in range(6):
    if sum(a) >= sum(b) and len(b) <= 3:
        b.append(lst[i])
    elif sum(a) < sum(b) and len(a) <= 3:
        a.append(lst[i])
    elif len(a) > 3:
        b.append(lst[i])
    elif len(b) > 3:
        a.append(lst[i])

print(abs(sum(a) - sum(b)))