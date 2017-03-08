def dijkstra1(A, start):
    used = [0] * n
    min_d = 0
    d = [float('+inf') for v in A]
    d[start] = 0
    path = [None]*n
    while min_d < float('+inf'):
        current = start
        used[current] = 1
        for neighbour in A[current]:
            l = d[current] + neighbour[1]
            if l < d[neighbour[0]]:
                d[neighbour[0]] = l
                path[neighbour[0]] = current
        min_d = float('+inf')
        for current in range(n):
            if (used[current] != 1) and (d[current] < min_d):
                start = current
                min_d = d[current]
    return path

n, m, s, f = map(int, input().split())
massiv = [[] for i in range(n)]
for j in range(m):
    a1, a2, q = map(int, input().split())
    massiv[a1].append([a2, q])
    massiv[a2].append([a1, q])
path = dijkstra1(massiv, s)
path_new = []
i = f
while i is not None:
    path_new.append(i)
    i = path[i]
path_new = path_new[::-1]
print(*path_new)
