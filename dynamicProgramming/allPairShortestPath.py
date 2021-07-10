# also know as Floyd Warshall's Algorithm

v = 4 # number of vertices
INF = 99999

def floydWarshall(graph):
    
    dist = []
    for i in range(v):
            dist.append(graph[i])
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print(dist)

graph = [[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0]]

floydWarshall(graph)