import heapq

def solution(k, score):
    answer = []
    hq = []
    for s in score:
        if len(hq) < k:
            heapq.heappush(hq, s)
            answer.append(hq[0])
        else:
            if hq[0] < s:
                heapq.heappop(hq)
                heapq.heappush(hq, s)
            answer.append(hq[0])
        
    return answer