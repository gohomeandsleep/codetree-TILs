input()
num_list=list(map(int, input().split()))

num_list_s = sorted(num_list)
print(*num_list_s)

num_list_r = sorted(num_list, reverse = True)
print(*num_list_r)