from collections import defaultdict
import heapq
def solution(N, road, K):
    edges = defaultdict(list)
    for r in road:
        edges[r[0]].append([r[1], r[2]])
        edges[r[1]].append([r[0], r[2]])
        
    dists = [500001 for _ in range(N + 1)]
    dists[1] = 0
    hq = []
    heapq.heappush(hq, [0, 1])
    while hq:
        cur_weight, cur_node = heapq.heappop(hq)
        if cur_weight > dists[cur_node]:
            continue
        for node, weight in edges[cur_node]:
            dist = cur_weight + weight
            if dist < dists[node]:
                dists[node] = dist
                heapq.heappush(hq, [dist, node])
    answer = 0
    for dist in dists:
        if dist <= K:
            answer += 1
    return answer