class user():
    def __init__(self, name: str, scores: tuple[int, int, int]):
        self.name = name
        self.scores = scores

N = int(input())
A = []
for _ in range(N):
    name, *scores = input().split()
    scores = tuple(map(int, scores))
    User = user(name, scores)
    A.append(User)

A.sort(key=lambda st: sum(st.scores))

for st in A:
    print(st.name, *st.scores)