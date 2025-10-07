from itertools import permutations

def solution(k, dungeons):
    answer = -1
    routes = permutations(dungeons)
    for route in routes:
        count = 0
        hp = k
        for dungeon in route:
            if hp >= dungeon[0]:
                count += 1
                hp -= dungeon[1]
            else:
                break
        answer = max(count, answer)
    return answer