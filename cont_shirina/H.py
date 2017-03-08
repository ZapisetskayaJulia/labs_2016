from heapq import *
def dijkstra(A, start):
    d = [float('+inf') for v in A]
    B = [[] for i in range(n)]
    B[start] = start
    d[start] = 0
    Q = [(start, 0)]
    used = set()
    while len(used) != n:
        current, d_current = heappop(Q)
        if d_current != d[current]:
            continue
        for neighbour in A[current]:
            l = d_current + neighbour[1]
            if l < d[neighbour[0]]:
                d[neighbour[0]] = l
                B[neighbour[0]] = B[current]
                B[neighbour[0]].append(neighbour[0])
                heappush(Q, (neighbour[0], l))
        used.add(current)
    return B

n, m, s, f = map(int, input().split())
massiv = [[] for i in range(n)]
for j in range(m):
    a1, a2, q = map(int, input().split())
    massiv[a1].append([a2, q])
    massiv[a2].append([a1, q])
path = dijkstra(massiv, s)[f]
print(*path)
