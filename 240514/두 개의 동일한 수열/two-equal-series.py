input()
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))

status = True

for i in range(len(a_list)):
    if a_list[i] != b_list[i]:
        status = False

if status == True:
    print("Yes")
else:
    print("No")