n = int(input())
lst = list(input())

res = 0
for i in range(n):
    if lst[i] == 'C':
        for j in range(i, n):
            if lst[j] == 'O':
                lst_part = lst[j:n+1]
                res += lst_part.count('W')

print(res)