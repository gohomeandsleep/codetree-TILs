lst = list(input())

res_lst = []
res_len = []

tmp = 1
for i in range(1,len(lst)):
    if lst[i] != lst[i-1]:
        res_lst.append(lst[i-1])
        res_len.append(tmp)
        tmp = 1
    else:
        tmp += 1
res_lst.append(lst[len(lst)-1])
res_len.append(tmp)

print(len(res_len) * 2)
for i in range(len(res_len)):
    print(res_lst[i], end='')
    print(res_len[i], end='')