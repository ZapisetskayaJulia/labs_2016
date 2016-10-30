m = int(input())
A = [['.']*m for i in range(m)]
for i in range(m):
    A[i][i] = '*'
    A[i][m-i-1] = '*'
    A[m//2][i] = '*'
    A[i][m//2] = '*'

for s in A:
   print(' '.join([str(i) for i in s]))