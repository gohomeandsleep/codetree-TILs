x1,y1,x2,y2 = map(int, input().split())
a1,b1,a2,b2 = map(int, input().split())

res = "overlapping"
if x2 < a1 or a2 < x1 or b2 < y1 or y2 < b1:
    res = "nonoverlapping"
print(res)