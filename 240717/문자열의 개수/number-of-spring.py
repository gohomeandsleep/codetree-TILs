lst = []
while True:
    tmp = input()
    if tmp == '0':
        break
    else:
        lst.append(tmp)

print(len(lst))
for i in range(len(lst)):
    if i % 2 == 0:
        print(lst[i])