from collections import Counter

def solution(clothes):
    types = []
    for item in clothes:
        types.append(item[1])
    type_counts = list(Counter(types).values())
    answer = 1
    for i in range(len(type_counts)):
        answer = answer * (type_counts[i]+1)
    return answer - 1