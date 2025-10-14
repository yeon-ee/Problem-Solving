from collections import deque

directions = [[1,0], [-1,0], [0,1], [0, -1]]

def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[False for _ in range(n)] for __ in range(m)]
    target = [n - 1, m - 1]
    q = deque([[0,0,1]])
    visited[0][0] = True
    while q:
        cur = q.popleft()
        if cur[:2] == target:
            return cur[2]
        for direction in directions:
            new_x = cur[0] + direction[0]
            new_y = cur[1] + direction[1]
            if 0 <= new_x < n and 0 <= new_y < m:
                if (not visited[new_y][new_x]) and maps[new_y][new_x] == 1:
                    visited[new_y][new_x] = True
                    q.append([new_x, new_y, cur[2] + 1])
    return -1