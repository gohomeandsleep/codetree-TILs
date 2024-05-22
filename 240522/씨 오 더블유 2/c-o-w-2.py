n = int(input())
lst = list(input())

res = 0
for i in range(n):
    if lst[i] == 'C':
        for j in range(i, n):
            if lst[j] == 'O':
                for k in range(j, n):
                    if lst[k] == 'W':
                        res+=1

print(res)