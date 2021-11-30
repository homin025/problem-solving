import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for y in range(1, N + 1):
        for x in range(1, M + 1):
            dp[y][x] = board[y - 1][x - 1] + dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1]

    K = int(input())
    for _ in range(K):
        y1, x1, y2, x2 = map(int, input().split())

        print(dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1])
