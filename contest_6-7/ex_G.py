def IsSymmetric(A):
    bool = True
    for i in range(len(A)):
        for j in range( len(A)):
            if A[i][j] != A[j][i]:
                bool = False
    return bool


m = int(input())
A = [[0]*m for i in range(m)]
for i in range(m):
    s = input().split()
    for j in range(m):
        A[i][j] = int(s[j])


truefalse = IsSymmetric(A)

if truefalse:
    print('YES')
else:
    print('NO')