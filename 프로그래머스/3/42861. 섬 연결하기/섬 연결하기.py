def solution(n, costs):
    moms = [i for i in range(n)]
    costs.sort(key= lambda x: x[2])
    def union(a, b):
        mom_a = moms[a]
        mom_b = moms[b]
        moms[mom_a] = mom_b
    def find(a):
        if moms[a] != a:
            moms[a] = find(moms[a])
        return moms[a]
    answer = 0
    for edge in costs:
        x, y, cost = edge
        if find(x) != find(y):
            union(x, y)
            answer += cost
    return answer