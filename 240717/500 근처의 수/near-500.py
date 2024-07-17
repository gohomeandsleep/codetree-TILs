lst = list(map(int, input().split()))
lst1 = []
lst2 = []
for i in lst:
    if i < 500:
        lst1.append(i)
    elif i > 500:
        lst2.append(i)

print(max(lst1), min(lst2))