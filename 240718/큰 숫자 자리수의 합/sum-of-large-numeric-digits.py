a,b,c = map(int, input().split())

res = a * b * c
res = list(str(res))
s = 0
for i in range(len(res)):
    s += int(res[i])
print(s)