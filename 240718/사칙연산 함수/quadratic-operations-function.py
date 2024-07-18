a, what, b = input().split()

if what == '+':
    print("%d + %d = %d" % (int(a), int(b), int(a) + int(b)))
elif what == '-':
    print("%d - %d = %d" % (int(a), int(b), int(a) - int(b)))
elif what == '*':
    print("%d * %d = %d" % (int(a), int(b), int(a) * int(b)))
elif what == '/':
    print("%d / %d = %d" % (int(a), int(b), int(a) // int(b)))
else:
    print('False')