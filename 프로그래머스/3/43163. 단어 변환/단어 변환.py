from collections import deque

def solution(begin, target, words):
    answer = 0
    words.append(begin)
    size = len(words[0])
    edges = [[] for _ in range(len(words))]
    for i in range(len(words)):
        for j in range(i, len(words)):
            compare = 0
            for index in range(size):
                if words[i][index] == words[j][index]:
                    compare += 1
            if compare == size - 1:
                edges[i].append(j)
                edges[j].append(i)
    q = deque([[len(words) - 1, 0]])
    visited = [False for _ in range(len(words))]
    while q:
        index, count = q.popleft()
        if words[index] == target:
            return count
        for next_index in edges[index]:
            if not visited[next_index]:
                visited[next_index] = True
                q.append([next_index, count + 1])
    return 0