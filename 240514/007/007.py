class Spy:
    def __init__ (self, secretCode, meetingPoint, time):
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time
    
sc, mp, t = input().split()
spy1 = Spy(sc, mp, t)
print(f"secret code : {spy1.secretCode}")

print(f"meeting point : {spy1.meetingPoint}")

print(f"time : {spy1.time}")