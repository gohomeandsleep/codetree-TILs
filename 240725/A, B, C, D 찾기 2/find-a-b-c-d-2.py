lst = list(map(int, input().split()))
abcd = max(lst)
lst.sort()

n = len(lst)
stat = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i == j or j == k or k == l or l == i or i == k or j == l or stat == False:
                    continue
                if lst[i] + lst[j] + lst[k] + lst[l] == abcd and lst[i] <= lst[j] <= lst[k] <= lst[l]:
                    tmp_lst = [lst[i], lst[j], lst[k], lst[l], lst[i]+lst[j], lst[i]+lst[k], lst[i]+lst[l],lst[j]+lst[k], lst[j]+lst[l],lst[k]+lst[l],lst[i]+lst[j]+lst[k],lst[i]+lst[j]+lst[l],lst[i]+lst[k]+lst[l],lst[l]+lst[j]+lst[k], abcd]
                    tmp_lst.sort()
                    if tmp_lst == lst:
                        print(lst[i], lst[j], lst[k], lst[l])
                        stat = False