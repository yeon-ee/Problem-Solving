from collections import deque

        
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0,0])
    while q:
        n, depth = q.popleft()
        if depth == len(numbers):
            if n == target:
                answer += 1
        else:
            q.append([n + numbers[depth], depth + 1])
            q.append([n - numbers[depth], depth + 1])
    return answer