def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam = -30001
    for car in routes:
        if car[0] <= cam:
            pass
        else:
            cam = car[1]
            answer += 1
    return answer