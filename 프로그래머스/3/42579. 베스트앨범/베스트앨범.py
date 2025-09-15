from collections import defaultdict

def solution(genres, plays):
    answer = []
    g_p = defaultdict(int)
    size = len(genres)
    for i in range(size):
        g_p[genres[i]] += plays[i]
    g_p = sorted(g_p.items(), key=lambda x:x[1],reverse=True)
    for i in range(len(g_p)):
        genre = g_p[i][0]
        gold = [None, 0]
        silver = [None, 0]
        for j in range(size):
            if genres[j] == genre:
                if plays[j] > gold[1]:
                    silver = gold
                    gold = [j, plays[j]]
                elif plays[j] > silver[1]:
                    silver = [j, plays[j]]
        answer.append(gold[0])
        if silver[0] is not None:
            answer.append(silver[0])
    return answer