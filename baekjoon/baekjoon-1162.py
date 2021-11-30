import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(graph, dists, K):
    heap = []
    heappush(heap, [0, 0, 1])

    while heap:
        curr_dist, curr_count, curr_city = heappop(heap)

        if curr_dist <= dists[curr_city][curr_count]:
            for next_city, next_cost in graph[curr_city]:
                if curr_dist + next_cost < dists[next_city][curr_count]:
                    dists[next_city][curr_count] = curr_dist + next_cost
                    heappush(heap, [curr_dist + next_cost, curr_count, next_city])
                if curr_count < K and curr_dist < dists[next_city][curr_count + 1]:
                    dists[next_city][curr_count + 1] = curr_dist
                    heappush(heap, [curr_dist, curr_count + 1, next_city])


if __name__ == "__main__":
    N, M, K = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(M):
        a, b, cost = map(int, input().split())

        graph[a].append([b, cost])
        graph[b].append([a, cost])

    # dists[v][k] = 1번 도시에서 v번 도시까지 k개의 도로가 포장되었을 때의 최솟값
    dists = [[sys.maxsize] * (K + 1) for _ in range(N + 1)]
    dists[1][0] = 0

    dijkstra(graph, dists, K)

    print(min(dists[N]))
