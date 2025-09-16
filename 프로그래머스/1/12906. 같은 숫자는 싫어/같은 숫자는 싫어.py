def solution(arr):
    answer = []
    curr = None
    for item in arr:
        if item != curr:
            answer.append(item)
            curr = item
    return answer