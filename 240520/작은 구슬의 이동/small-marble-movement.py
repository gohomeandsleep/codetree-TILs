n, t = map(int, input().split())
#n*n array, time
r,c,d = input().split()
#primary loc r->y, c->x, direction
r, c = int(r), int(c)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

direction = {
    'R' : 0,
    'L' : 1,
    'U' : 2,
    'D' : 3
}

c_dir = direction[d]
while t > 0:
    if c == 0:
        d = 'R'
    elif r == 0:
        d = 'D'
    elif c == n-1:
        d = 'L'
    elif r == n-1:
        d = 'U'
    else:
        c = c + dx[direction[d]]
        r = r + dy[direction[d]]
    print(c, r, d)
    t -= 1

print(c, r)