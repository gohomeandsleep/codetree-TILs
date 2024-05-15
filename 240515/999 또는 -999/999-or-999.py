num_list = list(map(int, input().split()))

if len(num_list) != 100:
    num_list.pop(-1)

print(max(num_list), min(num_list))