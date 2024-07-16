lst = [int(input()) for _ in range(10)]

mul3 = 0
mul5 = 0

for i in lst:
    if i % 3 == 0:
        mul3 += 1
    if i % 5 == 0:
        mul5 += 1

print(mul3, mul5)