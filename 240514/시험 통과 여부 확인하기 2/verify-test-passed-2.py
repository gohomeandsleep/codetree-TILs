std = int(input())

passstd = 0

for i in range(std):
    num_list = list(map(int, input().split()))
    avg = sum(num_list) / len(num_list)
    if avg >= 60:
        print("pass")
        passstd += 1
    else:
        print("fail")

print(passstd)