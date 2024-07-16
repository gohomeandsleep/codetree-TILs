lst = [int(input()) for _ in range(5)]

res = True
for i in lst:
    if i % 3 != 0:
        res = False

if res == True:
    print(1)
else:
    print(0)