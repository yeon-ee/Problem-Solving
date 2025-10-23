def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    for babo in lost:
        if babo in reserve:
            reserve.remove(babo)
            answer += 1
        elif (babo - 1) in reserve:
            reserve.remove(babo - 1)
            answer += 1
        elif (babo + 1) in reserve and (babo + 1) not in lost:
            reserve.remove(babo + 1)
            answer += 1
    
    return answer