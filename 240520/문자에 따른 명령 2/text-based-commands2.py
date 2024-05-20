inst = list(input())

x,y, rot = 0, 0, 40000

rot_x = [0, 1, 0, -1]
rot_y = [1, 0, -1, 0]

for i in range(len(inst)):
    if inst[i] == 'L':
        rot -= 1
    elif inst[i] == 'R':
        rot += 1 
    else:
        x += rot_x[rot % 4]
        y += rot_y[rot % 4]

print(x, y)