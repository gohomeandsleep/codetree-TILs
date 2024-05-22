lst = list(input())

cnt = 0
for i in range(len(lst)):
    if lst[i] == '(':
        for j in range(len(lst)-i):
            if lst[i+j] == ')':
                cnt +=1

print(cnt)