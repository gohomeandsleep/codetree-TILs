n, m = map(int, input().split())
lst = {}
for j in range(m):
    stp, endp = map(int, input().split())
    if endp > stp:
        stp, endp = endp, stp
    if (stp, endp) in lst:
        lst[(stp, endp)] += 1
    else:
        lst[(stp, endp)] = 1

max_value_key = max(lst, key=lst.get)
max_value = lst[max_value_key]
print(max_value)