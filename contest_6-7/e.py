s_0 = list(map(int, input().split()))
N = s_0[0]
M = s_0[1]
K = s_0[2]
n = []
m = []
s = [list('') for i in range(N)]
for i in range(N):
    for j in range(M):
        s[i].append(int(0))
for i in range(K):
    s_2 = list(map(int, input().split()))
    n.append(s_2[1] - 1)
    m.append(s_2[0] - 1)
for i in range(N):
    for j in range(M):
        for k in range(K):
            if i == m[k] and j == n[k]:
                s[i][j] = '*'
            elif i == m[k] - 1 and j == n[k]:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] + 1 and j == n[k]:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] and j == n[k] - 1:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] and j == n[k] + 1:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] - 1 and j == n[k] - 1:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] - 1 and j == n[k] + 1:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] + 1 and j == n[k] - 1:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
            elif i == m[k] + 1 and j == n[k] + 1:
                if s[i][j] != '*':
                    s[i][j] = int(s[i][j]) + 1
for i in range(N):
    print(*s[i])