def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = [0] + sorted(rocks) + [distance]
    ggs = [(sorted_rocks[i+1] - sorted_rocks[i]) for i in range(len(sorted_rocks) - 1)]
    # 0 2 11 14 17 21 25
    #  2 9  3  3  4  4
    def check(d):
        count = 0
        checking = 0
        while checking < len(ggs):
            checking_gg = ggs[checking]
            while checking_gg < d:
                count += 1
                checking += 1
                if checking < len(ggs):
                    checking_gg += ggs[checking]
                else: 
                    break
                if count > n:
                    return False
            checking += 1
        return count <= n
    
    def bs(start, end):
        if start >= end and check(start):
            return start
        mid = (start + end) // 2 + 1
        if check(mid):
            return bs(mid, end)
        else:
            return bs(start, mid - 1)
    
    return bs(1, 1e9)
