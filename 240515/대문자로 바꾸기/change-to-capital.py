char_list = [input().split() for _ in range(5)]

for i in range(5):
    for j in range(3):
        char_list[i][j] = char_list[i][j].upper()
        print(char_list[i][j], end=' ')
    print()