x1, x2, x3, x4 = map(int, input().split())
if x1 > x3:
    x1, x3 = x3, x1
    x2, x4 = x4, x2
if x2 >= x3:
    print("intersecting")
else:
    print("nonintersecting")