import sys
from collections import deque

input = sys.stdin.readline


def board_turn(board, R, C):
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]

    water = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == '*':
                for dir in range(4):
                    _r = r + dr[dir]
                    _c = c + dc[dir]

                    if 0 <= _r < R and 0 <= _c < C and board[_r][_c] != '*':
                        if board[_r][_c] != 'X' and board[_r][_c] != 'D':
                            water.append([_r, _c])

    for _r, _c in water:
        board[_r][_c] = '*'


if __name__ == "__main__":
    answer = "KAKTUS"

    R, C = map(int, input().split())

    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]

    board = [list(input().rstrip()) for _ in range(R)]
    visit = [[False] * C for _ in range(R)]

    S = None
    D = None

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'S':
                S = [r, c]
            elif board[r][c] == 'D':
                D = [r, c]

    time = 0

    queue = deque()
    queue.append([S[0], S[1], time])

    visit[S[0]][S[1]] = True

    while queue:
        curr_r, curr_c, curr_time = queue.popleft()

        if curr_r == D[0] and curr_c == D[1]:
            answer = str(curr_time)
            break

        if time <= curr_time:
            board_turn(board, R, C)
            time += 1

        for dir in range(4):
            next_r = curr_r + dr[dir]
            next_c = curr_c + dc[dir]

            if 0 <= next_r < R and 0 <= next_c < C:
                if not visit[next_r][next_c]:
                    if board[next_r][next_c] != '*' and board[next_r][next_c] != 'X':
                        queue.append([next_r, next_c, curr_time + 1])
                        visit[next_r][next_c] = True

    print(answer)
