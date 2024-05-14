num_list = list(map(int, input().split()))

if num_list[-1] == 0:
    for i in range(len(num_list) -1):
        print(num_list[len(num_list) - i - 2], end=' ')
else:
    for i in range(len(num_list)):
        print(num_list[len(num_list) - i - 1], end=' ')