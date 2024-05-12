cold_list = [0 for _ in range(3)]
temp_list = [0 for _ in range(3)]

emergencyCount = 0

for i in range(3):
    cold_list[i], temp_list[i] = input().split()
    temp_list[i] = int(temp_list[i])
    if cold_list[i] == 'Y' and temp_list[i] >= 37:
        emergencyCount += 1
    
if emergencyCount >= 2:
    print("E")
else:
    print("N")