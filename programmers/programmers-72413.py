import sys
from heapq import heappush, heappop


INF = sys.maxsize


def floyd_warshall(n, s, a, b, fares):
    answer = INF

    graph = [[INF] * (n+1) for _ in range(n+1)]
    for src, dst, cost in fares:
        graph[src][dst] = cost
        graph[dst][src] = cost

    for k in range(1, n+1):
        graph[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for t in range(1, n+1):
        answer = min(answer, graph[s][t] + graph[t][a] + graph[t][b])

    return answer


def dijkstra(n, s, a, b, fares):
    answer = INF

    graph = {n: {} for n in range(1, n+1)}
    for src, dst, cost in fares:
        graph[src][dst] = cost
        graph[dst][src] = cost

    dists = [[]]
    for start in range(1, n+1):
        dist = [INF for _ in range(n+1)]
        dist[start] = 0

        queue = []
        heappush(queue, (dist[start], start))
        while queue:
            cur_dist, cur_dst = heappop(queue)

            if cur_dist > dist[cur_dst]:
                continue
                
            for new_dst, new_dist in graph[cur_dst].items():
                if cur_dist + new_dist < dist[new_dst]:
                    dist[new_dst] = cur_dist + new_dist
                    heappush(queue, (cur_dist + new_dist, new_dst))
                    
        dists.append(dist)
        
    for t in range(1, n+1):
        answer = min(answer, dists[s][t] + dists[t][a] + dists[t][b])
        
    return answer


def solution(n, s, a, b, fares):
    answer = INF
    
    answer = dijkstra(n, s, a, b, fares)
    # answer = floyd_warshall(n, s, a, b, fares)

    return answer