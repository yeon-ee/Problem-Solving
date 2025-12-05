from collections import defaultdict
import heapq

def solution(n, costs):
    edges = defaultdict(list)
    for edge in costs:
        edges[edge[0]].append([edge[2], edge[1]])
        edges[edge[1]].append([edge[2], edge[0]])
    
    hq = []
    heapq.heappush(hq, [0, 0])
    visited = [False for _ in range(n)]
    count = 0
    answer = 0
    while hq :
        cur_cost, cur_node = heapq.heappop(hq)
        if not visited[cur_node]:
            count += 1
            visited[cur_node] = True
            answer += cur_cost
            for cost, next_node in edges[cur_node]:
                heapq.heappush(hq, [cost, next_node])
    return answer