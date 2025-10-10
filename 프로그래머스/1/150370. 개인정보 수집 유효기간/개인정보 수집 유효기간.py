def if_expired(today, init_date, duration):
    ty, tm, td = map(int, today.split("."))
    y, m, d = map(int, init_date.split("."))
    m += duration
    y += (m // 12)
    m = m % 12
    d -= 1
    if d == 0:
        m -= 1
        d = 28
    if m == 0:
        y -= 1
        m = 12
    if ty > y:
        return True
    elif ty == y and tm > m:
        return True
    elif ty == y and tm == m and td > d:
        return True
    else:
        return False
        
    
def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        a, n = term.split(" ")
        term_dict[a] = int(n)
    for i, pr in enumerate(privacies):
        dt, term = pr.split(" ")
        if if_expired(today, dt, term_dict[term]):
            answer.append(i + 1)
    return answer