lst = list(map(int, input().split()))
abcd = max(lst)

n = len(lst)
stat = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i == j or j == k or k == l or l == i or i == k or j == l or stat == False:
                    continue
                if lst[i] + lst[j] + lst[k] + lst[l] == abcd and lst[i] <= lst[j] <= lst[k] <= lst[l]:
                    print(lst[i], lst[j], lst[k], lst[l])
                    stat =False