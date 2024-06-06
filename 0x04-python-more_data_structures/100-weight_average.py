#!/usr/bin/python3
def weight_average(my_list: list = []) -> float:
    if my_list is None or len(my_list) == 0:
        return 0
    total = list(map(lambda x: x[0] * x[1], my_list))
    quotient = [x[1] for x in my_list]
    return sum(total) / sum(quotient)
