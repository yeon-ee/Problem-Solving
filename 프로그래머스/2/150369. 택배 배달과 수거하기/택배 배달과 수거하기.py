def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    for i in range(n-1, -1, -1):
        while deliveries[i] > 0 or pickups[i] > 0:
            if (deliveries[i] > 0 and d == 0) or (pickups[i] > 0 and p == 0):
                answer += (i+1) * 2
                d += cap
                p += cap
            if deliveries[i] > 0:
                if deliveries[i] > d:
                    deliveries[i] -= d
                    d = 0
                elif deliveries[i] <= d:
                    d -= deliveries[i]
                    deliveries[i] = 0
            if pickups[i] > 0:
                if pickups[i] > p:
                    pickups[i] -= p
                    p = 0
                elif pickups[i] <= p:
                    p -= pickups[i]
                    pickups[i] = 0
    return answer