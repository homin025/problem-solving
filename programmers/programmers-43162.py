from collections import deque


def dfs(n, computers, cur, visited):
    visited[cur] = True
    
    for nxt in range(n):
        if nxt == cur or visited[nxt] or computers[cur][nxt] == 0:
            continue
            
        visited[nxt] = True
        dfs(n, computers, nxt, visited)
    
    return


def bfs(n, computers, cur, visited):
    queue = deque()
    queue.append(cur)
    
    while queue:
        cur = queue.popleft()
        
        if visited[cur]:
            continue
        
        visited[cur] = True
        
        for nxt in range(n):
            if nxt == cur or visited[nxt] or computers[cur][nxt] == 0:
                continue
            
            queue.append(nxt)
            
    return


def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]
    for idx in range(n):
        if not visited[idx]:
            dfs(n, computers, idx, visited)
            # bfs(n, computers, idx, visited)
            answer += 1
    
    return answer