num_list = list(map(int, input().split()))

if (num_list[0] == min(num_list)):
    print(1)
else:
    print(0)

if (num_list[0] == num_list[1] and num_list[1] == num_list[2]):
    print(1)
else:
    print(0)