lst = list(input())

for i in range(len(lst)):
    if ord(lst[i]) >= 65 and ord(lst[i]) <= 90:
        print(chr(ord(lst[i]) + 32), end='')
    elif ord(lst[i]) >= 97 and ord(lst[i]) <= 122:
        print(lst[i], end='')
    elif ord(lst[i]) >= 48 and ord(lst[i]) <= 57:
        print(lst[i], end='')