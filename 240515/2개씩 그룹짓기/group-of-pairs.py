n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

new_num_list = []
for i in range(n):
    new_num_list.append(num_list[i] + num_list[2*n-i-1])
print(max(new_num_list))