import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())

    board = [0] + list(map(int, input().split()))

    logs = [0 for _ in range(N + 2)]
    for _ in range(M):
        a, b, k = map(int, input().split())
        logs[a] += k
        logs[b + 1] -= k

    sums = [0 for _ in range(N + 2)]
    for idx in range(1, N + 1):
        sums[idx] = sums[idx - 1] + logs[idx]
        board[idx] += sums[idx]

    print(' '.join(list(map(str, board[1:]))))
