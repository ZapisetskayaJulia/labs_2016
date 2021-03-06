#Сильно связный ли орграф?

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
            dfs(neighbour, graph, used)
    order.append(vertex)

def turn(graph):
    graph_new = [[] for i in range(N)]
    for i in range(N):
        for j in graph [i]:
            graph_new[j].append(i)
    return graph_new

def turnm(order):
    order_new = [0]*len(order)
    for i in range (len(order)):
        order_new [len(order)-i-1] = order[i]
    return order_new

N = int(input())
M = int(input())
graph = read_graph_as_lists(N,M)
used = set()
k = 0
order = []
for vertex in range(len(graph)):
    if vertex not in used:
        dfs(vertex, graph, used)

graph_new = turn(graph)
order_new = turnm(order)
used_new = set()
for vertex in order_new:
    if vertex not in used_new:
        dfs(vertex, graph_new, used_new)
        k += 1
if k == 1:
    print ('YES', k)
else:
    print ('NO',k)