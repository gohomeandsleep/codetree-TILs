lst = list(map(int, input().split()))

odd = []
even = []
for i in range(len(lst)):
    if i % 2 == 0:
        odd.append(lst[i])
    else:
        even.append(lst[i])

print(abs(sum(odd) - sum(even)))