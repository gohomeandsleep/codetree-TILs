a, b, c = map(int, input().split())

mxm = 0 
for i in range(1000):
    for j in range(1000):
        if a * i + b * j > c:
            break
        mxm = max(mxm, a*i + b*j)
print(mxm)