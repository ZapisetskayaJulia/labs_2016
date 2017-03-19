#Поиск кратчайшего пути между двумя узлами невзвешенного графа

def bfs (graph,start,fired= None):
    if fired is None:
        fired = set()
    fired.add(start)
    Q = [start]
    while Q:
        current = Q.pop(0)
        for neighbor in graph[current]:
            if neighbor not in fired:
                fired.add(neighbor)
                Q.append(neighbor)
                p[neighbor]+=p[current]


N, M, x, y = map (int,input().split())
graph = [[] for i in range(N)]
p =[1 for i in range (N)]
for i in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
p[x]=0
bfs(graph,x)
print(p[y])