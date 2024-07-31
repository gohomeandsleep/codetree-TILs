ex = list(input())

lst = []
for i in range(len(ex)):
    if ex[i] == '(':
        lst.append('(')
    else:
        lst.pop(-1)

if len(lst) == 0:
    print("Yes")
else:
    print("No")