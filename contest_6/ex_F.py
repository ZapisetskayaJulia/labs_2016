def SwapColumns(A, i, j):
    for k in range(len(A)):
        A[k][i], A[k][j] = A[k][j], A[k][i]
    return A


s = input().split()
n = int(s[0])
m = int(s[1])
A = [[0]*m for i in range(n)]
for i in range(n):
    s = input().split()
    for j in range(m):
        A[i][j] = int(s[j])

i, j = [int(k) for k in input().split()]

A = SwapColumns(A, i, j)

for s in A:
    print(' '.join([str(i) for i in s]))