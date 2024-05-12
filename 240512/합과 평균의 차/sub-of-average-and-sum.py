num_list = list(map(int, input().split()))

s_ = sum(num_list)
a_ = sum(num_list) / len(num_list)

print("%d\n%d\n%d" % (s_ , a_ , s_ - a_))