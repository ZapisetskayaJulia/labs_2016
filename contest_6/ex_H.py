def Transpose(A):
    l = len(A)
    l_1= len(A[0])
    new = [[0] * l for i in range(l_1)]
    for i in range(l):
        for j in range( l_1):
             new[j][i] = A[i][j]
    return new

s = input().split()
n = int(s[0])
m = int(s[1])
A = [[0]*m for i in range(n)]
for i in range(n):
    s = input().split()
    for j in range(m):
        A[i][j] = int(s[j])


new = Transpose(A)

for s in new:
    print(' '.join([str(i) for i in s]))