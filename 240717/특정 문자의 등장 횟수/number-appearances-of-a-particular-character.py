lst = list(input())

ee = 0
eb = 0
for i in range(1, len(lst)):
    if lst[i-1] == 'e' and lst[i] == 'e':
        ee +=1
    if lst[i-1] == 'e' and lst[i] == 'b':
        eb +=1
print(ee, eb)