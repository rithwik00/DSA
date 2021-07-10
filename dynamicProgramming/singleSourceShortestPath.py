# also know as DJIKSTRA's Algorithm

def shortestDistance(graph):
    global INF
    dist = [0] * N
    # print(dist)
    for i in range(N-2, -1, -1):
        dist[i] = INF
        for j in range(N):
            if graph[i][j] == INF:
                continue
            dist[i] = min(dist[i], graph[i][j] + dist[j])
            
            # print(i, '= i', j, '= j', dist, dist[i], graph[i][j], dist[j])

    return dist[0]

N = 8
INF = 999999999999
 
graph = [[INF, 1, 2, 5, INF, INF, INF, INF],
         [INF, INF, INF, INF, 4, 11, INF, INF],
         [INF, INF, INF, INF, 9, 5, 16, INF],
         [INF, INF, INF, INF, INF, INF, 2, INF],
         [INF, INF, INF, INF, INF, INF, INF, 18],
         [INF, INF, INF, INF, INF, INF, INF, 13],
         [INF, INF, INF, INF, INF, INF, INF, 2]]

print(shortestDistance(graph))