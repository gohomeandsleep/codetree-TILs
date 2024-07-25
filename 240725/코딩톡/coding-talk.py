people, talk, check = map(int, input().split())
lst = [chr(65+i) for i in range(people)]
chat = [list(input()) for _ in range(talk)]

if chat[check-1][2] == '0': #안 읽은 사람이 0명인 경우 -> 출력할게 없음
    print('')
else:
    lst.remove(chat[check-1][0])
    for i in range(check, people):
        try:
            lst.remove(chat[i][0])
        except:
            print('', end='')
    #print(lst)
    for j in range(0, check-1):
        if chat[j][2] == chat[check-1][2]:
            #print(chat[j][2], chat[check-1][2])
            try:
                lst.remove(chat[j][0])
            except:
                print('', end='')
    print(*lst, sep=' ')