lst = list(map(int, input().split()))
lst.sort()

stat = False
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i == j or j == k or k == i:
                continue
            tmp = [lst[i], lst[j], lst[k], lst[i]+lst[j] , lst[j]+lst[k], lst[k]+lst[i], lst[i]+lst[j]+lst[k]]
            tmp.sort()
            if lst == tmp and stat == False:
                print(lst[i], lst[j], lst[k])
                stat = True