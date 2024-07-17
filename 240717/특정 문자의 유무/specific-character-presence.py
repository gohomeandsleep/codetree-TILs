lst = list(input())

ee = 'No'
ab = 'No'
for i in range(1, len(lst)):
    if lst[i-1] == 'e' and lst[i] == 'e':
        ee = 'Yes'
    if lst[i-1] == 'a' and lst[i] == 'b':
        ab = 'Yes'
print(ee, ab)