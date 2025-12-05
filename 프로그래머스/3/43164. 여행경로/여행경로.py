from collections import defaultdict, deque
from copy import deepcopy

def solution(tickets):
    roads = defaultdict(list)
    for i, ticket in enumerate(tickets):
        roads[ticket[0]].append([ticket[1], i])
    routes = []
    q = deque()
    q.append([['ICN'], [False for _ in range(len(tickets))]])
    while q:
        route, used = q.pop()
        if len(route) == len(tickets) + 1:
            routes.append(route)
        cur_port = route[-1]
        for next_road in roads[cur_port]:
            if not used[next_road[1]]:
                cur_used = deepcopy(used)
                cur_route = deepcopy(route)
                cur_used[next_road[1]] = True
                cur_route.append(next_road[0])
                q.append([cur_route, cur_used])
    return sorted(routes)[0]