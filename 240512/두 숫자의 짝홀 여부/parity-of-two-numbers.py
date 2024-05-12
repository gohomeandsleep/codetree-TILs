num_list= list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        print("even")
    else:
        print("odd")