ex = list(input())

lst = []
for i in range(len(ex)):
    if ex[i] == '(':
        lst.append('(')
    elif ex[i] == ')' and len(lst) > 0:
        lst.pop(-1)
    else:
        lst.append(-1)
        break


if len(lst) == 0:
    print("Yes")
else:
    print("No")