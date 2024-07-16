a, b, c = map(int, input().split())

res= True

for i in range(a, b+1):
    if i % c == 0:
        res = False

if res == True:
    print("YES")
else:
    print("NO")