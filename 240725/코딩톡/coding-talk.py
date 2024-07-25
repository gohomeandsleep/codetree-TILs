people, talk, check = map(int, input().split())
lst = [chr(65+i) for i in range(people)]

for i in range(talk):
    person, unseen = input().split()
    if i >= check - 1:
        if person in lst:
            lst.remove(person)
print(*lst, sep=' ')