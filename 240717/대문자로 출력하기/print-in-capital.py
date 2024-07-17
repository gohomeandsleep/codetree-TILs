lst = list(input())

for i in range(len(lst)):
    if ord(lst[i]) >= 65 and ord(lst[i]) <= 90:
        print(lst[i], end='')
    elif ord(lst[i]) >= 97 and ord(lst[i]) <= 122:
        print(chr(ord(lst[i]) - 32), end='')