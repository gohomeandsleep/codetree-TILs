height, width = map(int, input().split())

def in_range(x, y):
    return 0<=x and x < width and 0 <= y and y < height

written_check = [[0 for _ in range(width)] for _ in range(height)]
result = [[0 for _ in range(width)] for _ in range(height)]

dxs = [1,0,-1,0]
dys = [0,-1,0,1]

x=0
y=0
direction = 0

for i in range(height * width):
    if not in_range or written_check[x][y] == 1:
        direction = (direction + 1) % 4

    written_check[x][y] = 1
    result[x][y] = i+1

    x += dxs[direction]
    y += dys[direction]
      

for _ in range(height):
    print(result)