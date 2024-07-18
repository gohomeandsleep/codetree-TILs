def is_valid(y, m, d):
    lst = [31, 28, 31,30,31,30,31,31,30,31,30,31]

    if y % 400 == 0:
        lst[1] = 29
    elif y % 100 == 0:
        lst[1] = 28
    elif y % 4 == 0:
        lst[1] = 29
    else:
        lst[1] = 28

    try:
        if d > lst[m-1]:
            return False
        else:
            return True
    except:
        return True

y, m, d = map(int, input().split())

if is_valid(y, m, d) == True:
    if m >= 3 and m <= 5:
        print('Spring')
    elif m >= 6 and m <= 8:
        print('Summer')
    elif m >= 9 and m <= 11:
        print('Fall')
    else:
        print("Winter")
else:
    print(-1)