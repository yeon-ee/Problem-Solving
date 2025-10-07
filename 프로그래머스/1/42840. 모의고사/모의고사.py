mapping_2 = {
    2: 1,
    4: 3,
    6: 4,
    0: 5
}

mapping_3 = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 4,
    8: 4,
    9: 5,
    0: 5
}

def solution(answers):
    result = [0] * 3
    for i in range(len(answers)):
        index = i + 1
        if index % 5 == answers[i] % 5:
            result[0] += 1
        if index % 2 == 1:
            if answers[i] == 2:
                result[1] += 1
        elif mapping_2[index % 8] == answers[i]:
            result[1] += 1
        if mapping_3[index % 10] == answers[i]:
            result[2] += 1
    max_score = max(result)
    answer = []
    for i in range(3):
        if max_score == result[i]:
            answer.append(i+1)
    return answer