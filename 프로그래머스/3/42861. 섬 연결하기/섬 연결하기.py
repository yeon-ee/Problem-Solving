from collections import defaultdict
import heapq

def solution(n, costs):
    answer = 0
    edges = defaultdict(list)
    for edge in costs:
        edges[edge[0]].append([edge[1], edge[2]])
        edges[edge[1]].append([edge[0], edge[2]])
    
    visited = [False for _ in range(n)]
    hq = [[0, 0]]
    count = 0
    while hq:
        if count == n:
            break
        cur_cost, cur_node = heapq.heappop(hq)
        if not visited[cur_node]:
            visited[cur_node] = True
            answer += cur_cost
            count += 1
        for next_node, next_cost in edges[cur_node]:
            if not visited[next_node]:
                heapq.heappush(hq, [next_cost, next_node])
    return answer