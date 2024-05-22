lst = list(input())

open = '('
close = ')'
cnt = 0

for i in range(len(lst)-1):
    if lst[i] == open and lst[i+1] == open:
        for j in range(i+2, len(lst)-1):
            if lst[j] == close and lst[j+1] == close:
                cnt += 1
print(cnt)