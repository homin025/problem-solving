

def solution(board, skill):
    answer = 0
    
    N = len(board)
    M = len(board[0])
    
    blocks = {}
    
    for type, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                id = i*M+j
                if type == 1:
                    if id not in blocks:
                        blocks[id] = board[i][j]
                    blocks[i*M+j] -= degree
                elif type == 2:
                    if id not in blocks:
                        blocks[id] = board[i][j]
                    blocks[i*M+j] += degree
    
    answer = M * N
    
    for block in blocks:
        if blocks[block] <= 0:
            answer -= 1
    
    return answer
