class Person:
    def __init__(self, name=0, height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = []
for _ in range(n):
    name, height, weight = input().split()
    people.append(Person(name, int(height), int(weight)))

people.sort(key=lambda x: x.height)

for p in people:
    print(p.name, p.height, p.weight)