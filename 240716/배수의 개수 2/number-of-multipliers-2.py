lst = [int(input()) for _  in range(10)]

res = 0
for i in lst:
    if i % 2 == 0:
        res += 1

print(res)