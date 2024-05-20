lst = list(map(int , list(input())))
len_lst = len(lst)

num = 0
for i in range(len_lst):
    num = num * 2 + lst[i]

print(num)