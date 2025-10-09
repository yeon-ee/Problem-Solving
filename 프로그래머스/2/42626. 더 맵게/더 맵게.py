import heapq

def solution(scoville, K):
    q = scoville
    heapq.heapify(q)
    count = 0
    while q[0] < K:
        if len(q) == 1:
            return -1
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        count += 1
        mix = first + second * 2
        heapq.heappush(q, mix)
    return count