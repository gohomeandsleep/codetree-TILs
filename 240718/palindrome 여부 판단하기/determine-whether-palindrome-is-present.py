lst = list(input())

res = 'Yes'
for i in range(len(lst) // 2):
    if lst[i] != lst[len(lst)-i-1]:
        res = 'No'

print(res)