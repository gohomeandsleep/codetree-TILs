num = int(input())
num_list = list(map(float, input().split()))

avg = sum(num_list) / len(num_list)

print("%.1f" % avg)
if avg >= 4:
    print("Perfect")
elif avg >= 3:
    print("Good")
else:
    print("Poor")