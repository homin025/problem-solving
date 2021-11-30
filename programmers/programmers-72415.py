from collections import deque
from itertools import permutations


answer = 1e10


def bfs(board, src, dst):
    src_r, src_c = src
    
    DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    queue = deque()
    queue.append((src_r, src_c, 0))
    
    check = set()
    check.add((src_r, src_c))
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == dst:
            break
            
        for dr, dc in DELTA:
            tmp_r, tmp_c = r + dr, c + dc
            
            # CURSOR
            if 0 <= tmp_r < 4 and 0 <= tmp_c < 4 and (tmp_r, tmp_c) not in check:
                queue.append((tmp_r, tmp_c, dist+1))
                check.add((tmp_r, tmp_c))
            
            # CTRL + CURSOR
            while 0 <= tmp_r < 4 and 0 <= tmp_c < 4 and board[tmp_r][tmp_c] == 0:
                tmp_r, tmp_c = tmp_r + dr, tmp_c + dc
                
            if not (0 <= tmp_r < 4 and 0 <= tmp_c < 4):
                tmp_r, tmp_c = tmp_r - dr, tmp_c - dc
                
            if (tmp_r, tmp_c) not in check:
                queue.append((tmp_r, tmp_c, dist+1))
                check.add((tmp_r, tmp_c))
            
    return dist


def backtracking(board, cards, perm, coord, dist):
    global answer
    
    if not perm:
        answer = dist if answer > dist else answer
        return
    
    card = perm[0]
    perm = perm[1:]
    
    card_A, card_B = cards[card]
    
    dist_A = dist + bfs(board, coord, card_A)
    dist_A += bfs(board, card_A, card_B)
    
    remove_card(board, cards, card)
    backtracking(board, cards, perm, card_B, dist_A+2)
    restore_card(board, cards, card)
    
    dist_B = dist + bfs(board, coord, card_B)
    dist_B += bfs(board, card_B, card_A)
    
    remove_card(board, cards, card)
    backtracking(board, cards, perm, card_A, dist_B+2)
    restore_card(board, cards, card)


def remove_card(board, cards, card):
    for r, c in cards[card]:
        board[r][c] = 0


def restore_card(board, cards, card):
    for r, c in cards[card]:
        board[r][c] = card


def solution(board, r, c):
    global answer
    
    cards = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in cards:
                    cards[board[i][j]] = [(i, j)]
                else:
                    cards[board[i][j]].append((i, j))
    
    perms = list(permutations(cards.keys(), len(cards.keys())))
    for perm in perms:
        backtracking(board, cards, perm, (r, c), 0)
        
    return answer