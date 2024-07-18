dd, dh, dm = map(int ,input().split())
pd, ph, pm = 11, 11, 11
elapsed_time = 0

while True:
    if pd == dd and ph == dh and pm == dm:
        break

    elapsed_time += 1
    pm += 1

    if pm > 60:
        ph += 1
        pm -= 60
    
    if ph > 24:
        pd += 1
        ph -= 24

print(elapsed_time)