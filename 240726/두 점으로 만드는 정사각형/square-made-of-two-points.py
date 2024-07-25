x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

stpx = min(x1, a1)
stpy = min(y1, b1)
endx = max(x2, a2)
endy = max(y2, b2)

print(max((endx - stpx) ,(endy - stpy)) ** 2)