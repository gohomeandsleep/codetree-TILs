class Person:
    def __init__(self,name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
people = []
for _ in range(n):
    name, kor, eng, math = input().split()
    people.append(Person(name, int(kor), int(eng), int(math)))

people.sort(key = lambda x : (-x.kor, -x.eng, -x.math))

for st in people:
    print(st.name, st.kor, st.eng, st.math)