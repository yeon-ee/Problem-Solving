N, M = map(int, input().split())
true_man_list = list(map(int, input().split()))
if true_man_list[0] != 0:
    true_man_list = true_man_list[1:]

moms = [i for i in range(N+1)]

def union(a, b):
    mom_a = find(a)
    mom_b = find(b)
    moms[mom_a] = mom_b

def find(a):
    if moms[a] != a:
        moms[a] = find(moms[a])
    return moms[a]

parties = []

for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(party)
    party_count = party[0]
    party_people = party[1:]
    for i in range(party_count - 1):
        union(party_people[i], party_people[i + 1])

answer = 0

for party in parties:
    party_people = party[1:]
    can_lie = True
    for pp in party_people:
        for true_man in true_man_list:
            if find(pp) == find(true_man):
                can_lie = False
    if can_lie:
        answer += 1
print(answer)