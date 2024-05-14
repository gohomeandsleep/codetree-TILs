num = int(input())
num_list = list(map(int, input().split()))
new_arr = [elem**2 for elem in num_list]

for i in range(len(num_list)):
    print(new_arr[i], end=' ')