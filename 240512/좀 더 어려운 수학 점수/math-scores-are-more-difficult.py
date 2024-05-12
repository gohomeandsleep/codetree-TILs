amath, aeng = map(int, input().split())
bmath, beng = map(int, input().split())

if amath > bmath:
    print("A")
elif amath < bmath:
    print("B")
else:
    if aeng > beng:
        print("A")
    elif aeng < beng:
        print("B")