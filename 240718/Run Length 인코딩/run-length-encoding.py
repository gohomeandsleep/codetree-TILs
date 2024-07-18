lst = input()

res_str = []
tmp = 1
for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:
        res_str.append(lst[i - 1])
        res_str.append(str(tmp))
        tmp = 1
    else:
        tmp += 1
res_str.append(lst[-1])
res_str.append(str(tmp))

result = ''.join(res_str)
print(len(result))
print(result)