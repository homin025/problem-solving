import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


parents = [0] * 100001
dists = [0] * 100001


def find(a):
    if parents[a] == a:
        return a
    else:
        parent = find(parents[a])
        dists[a] += dists[parents[a]]
        parents[a] = parent
        return parents[a]


def union(a, b, w):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        dists[root_b] = dists[a] - dists[b] + w
        parents[root_b] = root_a


if __name__ == "__main__":
    N, M = 1, 1

    while N | M:
        N, M = map(int, input().split())

        for idx in range(1, N + 1):
            parents[idx] = idx
            dists[idx] = 0

        for _ in range(M):
            cmds = input().split()

            if cmds[0] == "!":
                a, b, w = map(int, cmds[1:])

                union(a, b, w)

            elif cmds[0] == "?":
                a, b = map(int, cmds[1:])

                if find(a) == find(b):
                    print(dists[b] - dists[a])
                else:
                    print("UNKNOWN")
