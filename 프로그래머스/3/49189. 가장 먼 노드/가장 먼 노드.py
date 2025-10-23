from collections import defaultdict, deque

def solution(n, edge):
    edges = defaultdict(list)
    for a, b in edge:
        edges[a].append(b)
        edges[b].append(a)
    visited = [True] + [False for _ in range(n)]
    q = deque([[1, 0]])
    farest = 0
    answer = 0
    visited[1] = True
    while q:
        v, level = q.popleft()
        if level == farest:
            answer += 1
        elif level > farest:
            answer = 1
            farest = level
        for next_v in edges[v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append([next_v, level + 1])
    return answer