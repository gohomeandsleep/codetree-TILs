lst = list(map(int, input().split()))
lst.sort()

stat = False
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            for l in range(len(lst)):
                if i == j or j == k or k == l or l == i or i == k or j == l:
                    continue
                A, B, C, D = lst[i], lst[j], lst[k], lst[l]
                tmp = [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]
                tmp.sort()
                if lst == tmp and stat == False:
                    print(lst[i], lst[j], lst[k], lst[l])
                    stat = True