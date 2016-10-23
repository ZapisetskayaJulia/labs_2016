def Rotate(A):
    l = len(A)
    for i in range(l//2):
        for j in range(l//2,l):
            A[j][l-i-1], A[l-i-1][l-j-1], A[l-j-1][i], A[i][j] = A[i][j],A[j][l-i-1],A[l-i-1][l-j-1],A[l-j-1][i]

    for s in A:
        print(' '.join([str(i) for i in s]))


m = int(input())
A = [[0]*m for i in range(m)]
for i in range(m):
    s = input().split()
    for j in range(m):
        A[i][j] = int(s[j])


Rotate(A)

