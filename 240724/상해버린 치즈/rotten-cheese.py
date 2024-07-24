def has_common_element(list1, list2):
    set1 = set(tuple(sublist) for sublist in list1)
    set2 = set(tuple(sublist) for sublist in list2)
    
    return not set1.isdisjoint(set2)

n, m, d, s = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(d)]
sick = [list(map(int, input().split())) for _ in range(s)]

mxm = 0
for i in range(1, m + 1): #상한 치즈
    stat = True
    for j in range(s): #배가 아픈 사람들 모두 검증
        tmp = []
        for k in range(1, sick[j][1]):
            tmp.append([sick[j][0], i, k])
        if has_common_element(cheeze,tmp) == False:
            stat = False
    if stat == True:
        cheezelst = []
        for j in range(d):
            if cheeze[j][1] == i and cheeze[j][0] not in cheezelst:
                cheezelst.append(cheeze[j][0])
        mxm = max(mxm, len(cheezelst))
print(mxm)