s = list(map(int,input().split()))
N = s[0]
M = s[1]
K = s[2]
a = []
b = []
A = [list('') for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i].append(int(0))
for i in range(K):
    s_2  = list(map(int,input().split()))
    b.append(s_2[0] - 1)
    a.append(s_2[1] - 1)
for i in range(N):
    for j in range(M):
        for k in range(K):
            if i == b[k] and j == a[k]:
                A[i][j] = '*'
            elif i == b[k] + 1 and j == a[k]:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k] - 1 and j == a[k]:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k]  and j == a[k] + 1:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k]  and j == a[k] - 1:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k] + 1 and j == a[k] - 1:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k] + 1 and j == a[k] + 1:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k] - 1 and j == a[k] + 1:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
            elif i == b[k] + 1 and j == a[k] - 1:
                if A[i][j] != '*':
                    A[i][j] = int(A[i][j])+1
for i in range(N):
    print(*s[i])