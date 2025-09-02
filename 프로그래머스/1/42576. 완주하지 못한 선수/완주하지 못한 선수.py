from collections import Counter

def solution(participant, completion):
    answer_dict = Counter(participant) - Counter(completion)
    return list(answer_dict.keys())[0]