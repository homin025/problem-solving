import copy
from collections import defaultdict, deque


def bfs(info, adj, curr, queue, visit, sheep, wolf):
    global answer

    if info[curr] == 0:
        sheep += 1
    else:
        wolf += 1

    answer = answer if answer > sheep else sheep
    if sheep <= wolf:
        return
        
    visit[curr] = True
    for node in adj[curr]:
        if not visit[node]:
            if node not in queue:
                queue.append(node)
                
    for node in queue:
        _visit = copy.deepcopy(visit)
        _queue = copy.deepcopy(queue)
        _queue.remove(node)
        bfs(info, adj, node, _queue, _visit, sheep, wolf)


def solution(info, edges):
    global answer
    answer = 0
    
    adj = defaultdict(list)
    for edge in edges:
        fr, to = edge
        adj[fr].append(to)
        
    queue = []
    visit = [False for _ in range(len(info)+1)]
    bfs(info, adj, 0, copy.deepcopy(queue), copy.deepcopy(visit), 0, 0)

    return answer
