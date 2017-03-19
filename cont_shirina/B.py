#Построить остовное дерево обходом в ширину

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
                print(current,neighbor)


N, M = map (int,input().split())
graph = [[] for i in range(N)]
for i in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)



bfs(graph,0)