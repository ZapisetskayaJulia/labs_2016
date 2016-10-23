s = input().split()
n = int(s[0])
m = int(s[1])
A = [['.']*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)% 2 != 0:
            A[i][j] = '*'

for s in A:
    print(' '.join([str(i) for i in s]))