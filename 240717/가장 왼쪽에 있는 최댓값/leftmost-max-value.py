n = int(input())
lst = list(map(int, input().split()))
endp = n-1
while endp != 0:
    tmp = max(lst)
    endp = lst.index(tmp)
    print(endp + 1, end=' ')
    lst = lst[:endp]