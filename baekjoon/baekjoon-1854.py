import sys, math
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(graph, dists, K):
    heap = []
    heappush(heap, [0, 1])

    while heap:
        curr_dist, curr_node = heappop(heap)

        for next_node, next_dist in graph[curr_node]:
            if dists[next_node][K - 1] > curr_dist + next_dist:
                dists[next_node][K - 1] = curr_dist + next_dist
                dists[next_node].sort()

                heappush(heap, [curr_dist + next_dist, next_node])

    return -1


if __name__ == "__main__":
    N, M, K = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(M):
        a, b, c = map(int, input().split())

        graph[a].append([b, c])

    dists = [[sys.maxsize] * K for _ in range(N + 1)]
    dists[1][0] = 0

    dijkstra(graph, dists, K)

    for idx in range(1, N + 1):
        if dists[idx][K - 1] != sys.maxsize:
            print(dists[idx][K - 1])
        else:
            print(-1)
