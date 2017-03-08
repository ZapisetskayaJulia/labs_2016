def read_graph_as_lists(N,M):
    graph = [[] for i in range(N)]
    for edge in range (M):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
    return graph

def dfs(vertex, graph, used=set()):
    used.add(vertex)
    for neighbour in graph [vertex]:
        if neighbour not in used:
            a.append(neighbour)
            dfs(neighbour, graph, used)

def turn(graph):
    graph_new = [[] for i in range(N)]
    for i in range(N):
        for j in graph [i]:
            graph_new[j].append(i)
    return graph_new

def turnm(a):
    a_new = [0]*N
    for i in range (N):
        a_new [N-i-1] = a[i]
    return a_new

N = int(input())
M = int(input())
graph = read_graph_as_lists(N,M)
used = set()
k = 0
a = []
for vertex in range(len(graph)):
    if vertex not in used:
        a.append(vertex)
        dfs(vertex, graph, used)

graph_new = turn(graph)
a_new = turnm(a)
used_new = set()
for vertex in a_new:
    if vertex not in used_new:
        print('vertex', vertex)
        dfs(vertex, graph_new, used_new)
        k += 1
print(k)