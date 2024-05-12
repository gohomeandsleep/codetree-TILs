firsty, firsts = input().split()
secondy, seconds = input().split()

firsty = int(firsty)
secondy = int(secondy)

if firsty >= 19 and firsts == "M":
    print(1)
elif secondy >=19 and seconds == "M":
    print(1)
else:
    print(0)