def remove_substrings(A, B):
    while B in A:
        A = A.replace(B, '', 1)
    return A

A = input()
B = input()

result = remove_substrings(A, B)

print(result)