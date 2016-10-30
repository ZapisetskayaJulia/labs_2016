s = input().split()
n = int(s[0])
m = int(s[1])
A = [[0]*m for i in range(n)]
for i in range(n):
    s = input().split()
    for j in range(m):
        A[i][j] = int(s[j])

a = 0
b = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > A[a][b]:
            a, b = i, j

print(a, b)
#for s in A:
 #   print(' '.join([str(i) for i in s]))