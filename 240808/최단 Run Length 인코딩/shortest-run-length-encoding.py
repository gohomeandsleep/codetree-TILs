lst = list(input())

res = float('inf')
for _ in range(len(lst)):
    lst.append(lst.pop(0))
    p_sum = 0
    cnt = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            cnt += 1
        else:
            p_sum += 2
    
    if cnt == 10:
        p_sum += 3
    else:
        p_sum += 2
    res = min(res, p_sum)

print(res)