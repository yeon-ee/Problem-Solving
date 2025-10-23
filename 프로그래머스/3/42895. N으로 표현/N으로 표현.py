from collections import defaultdict

def solution(N, number):
    results = defaultdict(set)
    def cal(a, b):
        result = []
        for i in results[a]:
            for j in results[b]:
                result.append(i + j)
                result.append(i * j)
                if j != 0:
                    result.append(i // j)
                result.append(i - j)
        return result

    for n in range(1, 9):
        results[n].add(int(str(N) * n))
        for k in range(1, n):
            cal_result = cal(k, n-k)
            for c in cal_result:
                results[n].add(c)
    for n in range(1, 9):
        if number in results[n]:
            return n
    return -1