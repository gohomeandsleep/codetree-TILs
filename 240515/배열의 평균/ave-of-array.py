num_list = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    avg = sum(num_list[i]) / 4
    print("%.1f" % avg, end=' ')
print()

for i in range(4):
    avg = (num_list[0][i] + num_list[1][i]) / 2
    print("%.1f" % avg, end=' ')
print()

avg = (sum(num_list[0]) + sum(num_list[1])) / 8
print("%.1f" % avg, end=' ')