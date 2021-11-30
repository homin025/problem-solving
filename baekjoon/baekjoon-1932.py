import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    triangle = []
    for _ in range(N):
        triangle.append(list(map(int, input().split())))

    dp = [[0] * i for i in range(1, N + 1)]
    dp[0][0] = triangle[0][0]

    for height in range(1, N):
        for position in range(0, height + 1):
            if position == 0:
                dp[height][position] = triangle[height][position] + dp[height - 1][position]
            elif position == height:
                dp[height][position] = triangle[height][position] + dp[height - 1][position - 1]
            else:
                dp[height][position] = triangle[height][position] + max(dp[height - 1][position - 1], dp[height - 1][position])

    print(max(dp[N - 1]))
