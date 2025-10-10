from itertools import product
import copy

def discount_price(price, dis):
    return price * (100 - dis) / 100


def solution(users, emoticons):
    dis_club = {10: [], 20: [], 30: [], 40:[]}
    for i, user in enumerate(users):
        for dis in [10, 20, 30, 40]:
            if user[0] <= dis:
                dis_club[dis].append(i)
    max_plus = 0
    max_money = 0
    for dis_list in list(product([10,20,30,40], repeat=len(emoticons))):
        plus = 0
        money = 0
        user_list = copy.deepcopy(users)
        for user in user_list:
            user.append(0)
        for i, dis in enumerate(dis_list):
            p = discount_price(emoticons[i], dis)
            for user_index in dis_club[dis]:
                user_list[user_index][2] += p
        for user in user_list:
            if user[2] >= user[1]:
                plus += 1
            else:
                money += user[2]
        if max_plus < plus:
            max_plus = plus
            max_money = money
        elif max_plus == plus:
            if max_money < money:
                max_money = money
    return [max_plus, int(max_money)]