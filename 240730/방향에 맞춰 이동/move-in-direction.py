n = int(input())

dir_lst = ['N', 'S', 'E', 'W']
x_lst = [0,0,1,-1]
y_lst = [1,-1,0,0]
x,y = 0, 0
for i in range(n):
    dir, num = input().split()
    dir_num = int(dir_lst.index(dir))
    x = x + int(num) * x_lst[dir_num]
    y = y + int(num) * y_lst[dir_num]

print(x, y)