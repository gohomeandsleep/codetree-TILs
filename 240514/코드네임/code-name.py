class User:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

A = []
for _ in range(5):
    codename, score = input().split()
    user = User(codename, int(score))
    A.append(user)

ans_user = A[0]
for user in A:
    if ans_user.score > user.score:
        ans_user = user

print(ans_user.codename, ans_user.score)