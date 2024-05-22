lst = list(input())
for i in range(len(lst)):
    lst[i] = int(lst[i])
#print(lst)
for i in range(len(lst)):
    if lst[i] == 0:
        lst[i] = 1
        break
    else:
        continue
#print(lst)

res = 0
for i in range(len(lst)):
    #print(res, lst[i])
    res = res * 2 + lst[i]
    
print(res)