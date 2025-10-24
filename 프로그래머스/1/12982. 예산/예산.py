def solution(d, budget):
    d.sort()
    answer = 0
    i = 0
    while budget > 0 and i < len(d):
        if budget >= d[i]:
            answer +=1
            budget -= d[i]
        i += 1
    return answer