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

lst = []
for i in range(len(res_len)):
    lst.extend(list(str(res_lst[i])))
    lst.extend(list(str(res_len[i])))

print(len(lst))
print(*lst, sep='')