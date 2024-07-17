lst = ['apple', 'banana', 'grape', 'blueberry', 'orange']
llist = []

for i in range(len(lst)):
    llist.append(list(lst[i]))

c = input()
res = []
for i in range(5):
    if llist[i][2] == c or llist[i][3] == c:
        res.append(lst[i])
if res != []:
    print(*res, sep='\n')
print(len(res))