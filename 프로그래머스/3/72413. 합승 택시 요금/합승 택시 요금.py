# n = 6	
# s = 4	
# a = 6	
# b = 2	
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]#
# result = 82
# from+s [1000000000,10,66,51,0,34,35],[1000000000,25,48,26,35,2,0],[1000000000,63,0,22,66,46,48]
from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    answer = 0
    
    edges = defaultdict(list)
    for edge in fares:
        edges[edge[0]].append([edge[1], edge[2]])
        edges[edge[1]].append([edge[0], edge[2]])
    
    def dijkstra(start):
        dists = [1e9 for _ in range(n + 1)]
        dists[start] = 0
        hq = [[0, start]]
        
        while hq:
            cur_dist, cur_node = heapq.heappop(hq)
            
            if cur_dist > dists[cur_node]:
                continue
            
            for node, weight in edges[cur_node]:
                dist = cur_dist + weight
                if dist < dists[node]:
                    dists[node] = dist
                    heapq.heappush(hq, [dist, node])
        return dists
    from_s = dijkstra(s) #[1000000000,10,66,51,0 ,34,35]
    from_a = dijkstra(a) #[1000000000,25,48,26,35,2 ,0]
    from_b = dijkstra(b) #[1000000000,63,0 ,22,66,46,48]
    from_total = []
    for i in range(len(from_s)):
        from_total.append(from_s[i] + from_a[i] + from_b[i])
    return min(from_total)
